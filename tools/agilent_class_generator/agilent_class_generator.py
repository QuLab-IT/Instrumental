import argparse
import os
import re

from jinja2 import Environment, FileSystemLoader
from instrumental.parse_modules import generate_info_file
from parse_agilent_sdl import (
    CommandInfo,
    GlobalDefinition,
    Node,
    ParameterData,
    ParsedData,
    ResponseData,
    extract_supported_models,
    parse_sdl_file,
)
from typing import List, Dict, Any
from utils import sanitize_enum_name


# --- Start: Helper functions (adapted/copied from agilent_class_generator.py) ---
# These would be more complete in a full implementation.

def get_method_name(command_info: CommandInfo, is_query: bool, has_parameters: bool) -> str:
    base_name = "_".join(command_info.path).lower()
    if is_query:
        method_name = f"get_{base_name}"
    else:
        method_name = f"set_{base_name}" if has_parameters else base_name
    return method_name # Ensure method name is valid identifier


def generate_method_docstring(cmd_info: CommandInfo, is_write: bool, nodes: List[Node] = None) -> str:
    """
    Generate a docstring for a command method.

    Args:
        cmd_info: Command information dataclass
        is_write: Whether this is a write command
        nodes: List of nodes in the path that have suffixes

    Returns:
        str: The generated docstring
    """
    docstring = '''"""\n'''
    docstring += f"    {cmd_info.synopsis}\n\n"

    # Document parameters based on command type and available syntaxes
    has_parameters = is_write and cmd_info.command_syntaxes
    has_suffixes = nodes and any(node.suffixes for node in nodes)
    
    if has_parameters or has_suffixes:
        docstring += "    Args:\n"
        
        # Document node suffixes first
        if has_suffixes:
            for node in nodes:
                if node.suffixes:
                    suffix_name = f"{node.mnemonic.lower()}_{node.suffixes.name}"
                    docstring += f"        {suffix_name} (int): {node.suffixes.description}"
                    if node.suffixes.min_value is not None and node.suffixes.max_value is not None:
                        docstring += f" (Range: {node.suffixes.min_value}-{node.suffixes.max_value})"
                    docstring += "\n"

        # Document syntax parameter if multiple syntaxes
        if len(cmd_info.command_syntaxes) > 1:
            enum_name = f"{sanitize_enum_name('_'.join(cmd_info.path).upper())}Syntax"
            docstring += f"        syntax ({enum_name}): The syntax variant to use for this command\n"

        # Document command parameters for each syntax
        if has_parameters:
            for syntax in cmd_info.command_syntaxes:
                if len(cmd_info.command_syntaxes) > 1:
                    docstring += f"\n        For syntax {syntax.name}:\n"
                if syntax.parameters:
                    for param in syntax.parameters:
                        param_desc = f"{param.description}"
                        if param.repeat:
                            param_desc += f" (Repeatable: {param.repeat})"
                        if len(cmd_info.command_syntaxes) > 1:
                            docstring += f"            {param.name} ({(param.to_python_type())}): {param_desc}\n"
                        else:
                            docstring += f"        {param.name} ({param.to_python_type()}): {param_desc}\n"

    if not is_write and cmd_info.responses:
        docstring += "\n    Returns:\n"
        for response in cmd_info.responses:
            docstring += f"        {response.to_python_type()}: {response.description}\n"

    docstring += '''    """'''
    return docstring

def get_parameter_types(param: ParameterData, definitions: Dict[str, GlobalDefinition] = None) -> List[str]:
    types = []
    if param.parameter_types:
        for pt in param.parameter_types:
            if pt.enum_ref:
                # Ensure definitions is not None before accessing
                enum_original_name = definitions[pt.enum_ref].name if definitions and pt.enum_ref in definitions else pt.enum_ref
                type_name = sanitize_enum_name(enum_original_name)
            else:
                # Fallback to param.to_python_type() if pt doesn't have its own type string method
                # This assumes ParameterData.to_python_type() gives a basic type like 'int', 'str'
                # Or, if ParameterType (pt) had a method like pt.get_basic_type_str(), it would be used here.
                type_name = param.to_python_type()  
            if type_name not in types:
                types.append(type_name)
    if not types and param.type: # Fallback if parameter_types is empty but param.type exists
        py_type = param.to_python_type()
        if py_type:
            types.append(py_type)
            
    return types if types else ["Any"] # Default to Any if no types could be determined


def parameter_types_as_string(types: List[str]) -> str:
    if not types or "Any" in types and len(types) == 1: return "Any"
    # Filter out 'Any' if other types are present for the Union hint
    concrete_types = [t for t in types if t != "Any"]
    if not concrete_types: return "Any"

    if len(concrete_types) == 1: return concrete_types[0]
    return f"Union[{', '.join(concrete_types)}]"

def get_response_type(response: ResponseData, definitions: Dict[str, GlobalDefinition] = None) -> str:
    types = []
    if response.response_types:
        for rt in response.response_types:
            if rt.enum_ref:
                enum_original_name = definitions[rt.enum_ref].name if definitions and rt.enum_ref in definitions else rt.enum_ref
                type_name = sanitize_enum_name(enum_original_name)
            else:
                type_name = response.to_python_type() 
            if type_name not in types:
                types.append(type_name)
    
    actual_types = types if types else ["Any"]
    if len(actual_types) == 1: return actual_types[0]
    return f"Union[{', '.join(actual_types)}]"


def generate_binary_format_methods_code() -> str:
    # Copied from agilent_class_generator.generate_binary_format_methods()
    return '''
    def _set_binary_format(self, format_name: str) -> None:
        """Set the binary data format for subsequent commands.
        
        Args:
            format_name: The format name (e.g., 'BlockInt16', 'BlockReal32')
        """
        format_commands = {
            'BlockInt16': 'FORMat:BORDer SWAPped',
            'BlockReal32': 'FORMat:BORDer SWAPped',
            'BlockInt16xxx': 'FORMat:BORDer SWAPped',
            'BlockReal32xxx': 'FORMat:BORder SWAPped'
        }
        if format_name not in format_commands:
            raise ValueError(f"Unsupported binary format: {format_name}")
        self._rsrc.write(format_commands[format_name])

    def _prepare_binary_data(self, data: Any, format_name: str) -> bytes:
        """Prepare binary data according to the specified format.
        
        Args:
            data: The data to convert
            format_name: The format name (e.g., 'BlockInt16', 'BlockReal32')
            
        Returns:
            bytes: The prepared binary data
        """
        if format_name.startswith('BlockInt16'):
            if isinstance(data, (list, tuple, np.ndarray)):
                data = np.array(data, dtype=np.int16)
            else:
                data = np.array([data], dtype=np.int16)
            return data.tobytes()
            
        elif format_name.startswith('BlockReal32'):
            if isinstance(data, (list, tuple, np.ndarray)):
                data = np.array(data, dtype=np.float32)
            else:
                data = np.array([data], dtype=np.float32)
            return data.tobytes()
            
        else:
            raise ValueError(f"Unsupported binary format: {format_name}")

    def _write_binary_data(self, cmd: str, data: Any, format_name: str) -> None:
        """Write a command with binary data.
        
        Args:
            cmd: The SCPI command string
            data: The binary data to write
            format_name: The format name (e.g., 'BlockInt16', 'BlockReal32')
        """
        # Set the binary format
        self._set_binary_format(format_name)
        
        # Prepare the binary data
        binary_data = self._prepare_binary_data(data, format_name)
        
        # Write the command and data
        self._rsrc.write_binary_values(cmd, binary_data)
'''
# --- End: Helper functions ---

def _process_command_for_template(
    cmd_info: CommandInfo,
    is_query: bool,
    global_defs_map: Dict[str, GlobalDefinition],
    nodes_context: List[Node] = None
) -> Dict[str, Any]:
    cmd_dict: Dict[str, Any] = {}
    has_parameters = any(syntax.parameters for syntax in cmd_info.command_syntaxes)
    cmd_dict['method_name'] = get_method_name(cmd_info, is_query, has_parameters)
    cmd_dict['docstring'] = generate_method_docstring(cmd_info, is_write=not is_query, nodes=nodes_context)
    cmd_dict['is_query'] = is_query
    cmd_dict['has_write'] = cmd_info.has_write 

    params_sig_parts: List[str] = []
    validation_rules_list: List[Dict[str, Any]] = []

    cmd_dict['is_single_syntax'] = len(cmd_info.command_syntaxes) <= 1
    cmd_dict['syntaxes_info'] = []

    if not is_query: # Write command
        if not cmd_dict['is_single_syntax']: # Multi-syntax write
            syntax_enum_name = f"{sanitize_enum_name('_'.join(cmd_info.path).upper())}Syntax"
            cmd_dict['syntax_enum_name'] = syntax_enum_name
            params_sig_parts.append(f"syntax: {syntax_enum_name}")
            validation_rules_list.append({'name': 'syntax', 'type_options': [syntax_enum_name]})
            
            common_param_names = set()
            if cmd_info.command_syntaxes and cmd_info.command_syntaxes[0].parameters:
                common_param_names.update(p.name for p in cmd_info.command_syntaxes[0].parameters if p.name)
                for syn_obj in cmd_info.command_syntaxes[1:]:
                    if syn_obj.parameters:
                        common_param_names &= set(p.name for p in syn_obj.parameters if p.name)
                    else:
                        common_param_names.clear()
                        break
            
            added_common_params = set()
            if cmd_info.command_syntaxes and cmd_info.command_syntaxes[0].parameters:
                 for p_data_obj in cmd_info.command_syntaxes[0].parameters: 
                    if p_data_obj.name in common_param_names and p_data_obj.name not in added_common_params:
                        p_type_list = get_parameter_types(p_data_obj, global_defs_map)
                        p_type_str_for_sig = parameter_types_as_string(p_type_list)
                        params_sig_parts.append(f"{p_data_obj.name}: {p_type_str_for_sig}")
                        added_common_params.add(p_data_obj.name)
                        
                        validation_rules_list.append({
                            'name': p_data_obj.name, 
                            'type_options': p_type_list
                        })

            params_sig_parts.append("data: Any")
            validation_rules_list.append({'name': 'data', 'type_options': ['Any']})
            cmd_dict['common_param_names_for_multisyntax'] = list(common_param_names)

        elif cmd_info.command_syntaxes and cmd_info.command_syntaxes[0].parameters: # Single syntax write with SCPI params
            for p_data_obj in cmd_info.command_syntaxes[0].parameters:
                p_type_list = get_parameter_types(p_data_obj, global_defs_map)
                p_type_str_for_sig = parameter_types_as_string(p_type_list)
                params_sig_parts.append(f"{p_data_obj.name}: {p_type_str_for_sig}")

                validation_rules_list.append({
                    'name': p_data_obj.name, 
                    'type_options': p_type_list
                })

    if nodes_context:
        for node in nodes_context:
            if node.suffixes:
                suffix_var_name = f"{node.mnemonic.lower()}_{node.suffixes.name}"
                default_val = node.suffixes.min_value if node.suffixes.min_value is not None else 1
                params_sig_parts.append(f"{suffix_var_name}: int = {default_val}")
                
                rule = {'name': suffix_var_name, 'type_options': ['int']}
                if node.suffixes.min_value is not None:
                    rule['min_val'] = node.suffixes.min_value
                if node.suffixes.max_value is not None:
                    rule['max_val'] = node.suffixes.max_value
                validation_rules_list.append(rule)

    cmd_dict['parameters_signature_parts'] = params_sig_parts
    cmd_dict['parameter_validation_rules_repr'] = repr(validation_rules_list)

    if is_query and cmd_info.responses:
        response_type_list = get_response_type(cmd_info.responses[0], global_defs_map)
        # get_response_type already returns a string, potentially Union string or single type
        cmd_dict['return_type_annotation'] = f" -> {response_type_list}"
        cmd_dict['response_converter'] = cmd_info.responses[0].to_python_type_converter()
    elif not is_query:
        cmd_dict['return_type_annotation'] = " -> None"
    else: 
        cmd_dict['return_type_annotation'] = "" 

    # --- Start of replacement block for SCPI path and prefix generation ---
    # processed_path_parts will be the SCPI command string parts,
    # potentially with suffix placeholders like {suffix_var_name}.
    processed_path_parts = []
    
    # nodes_context provides information about suffixes for path parts.
    # Create a lookup map for nodes in the current context by their mnemonic.
    # Assuming node mnemonics in the map should be upper-cased for matching,
    # and cmd_info.path contains the SCPI keywords in their desired casing.
    node_mnemonic_map = {node.mnemonic.upper(): node for node in nodes_context} if nodes_context else {}

    for path_part_name in cmd_info.path:
        # Check if this part_name corresponds to a node in nodes_context that has a suffix.
        node_for_part = node_mnemonic_map.get(path_part_name.upper())
        
        if node_for_part and node_for_part.suffixes:
            # This part of the command corresponds to a node with a suffix.
            # The suffix variable name format is like "node_mnemonic_lower_suffix_name".
            suffix_var_name = f"{node_for_part.mnemonic.lower()}_{node_for_part.suffixes.name}"
            # Use the original path_part_name for casing, and append the suffix placeholder.
            processed_path_parts.append(f"{path_part_name}{{{suffix_var_name}}}")
        else:
            # No suffix for this part, or this part doesn't match a node with suffix in current context.
            processed_path_parts.append(path_part_name)

    # Determine SCPI command prefix
    scpi_cmd_prefix = ""  # Default
    is_direct_command = not nodes_context # True if it's a root-level command (no parent subsystem nodes in context)
    
    if processed_path_parts and processed_path_parts[0].startswith("*"):
        # Command already starts with '*', like *IDN, *OPC. No additional prefix needed.
        # The '*' is part of the first processed_path_part.
        scpi_cmd_prefix = ""
    elif is_direct_command:
        # Direct command that does not start with '*', e.g., WAI, ABORt. Needs '*' prefix.
        scpi_cmd_prefix = "*"
    else: # Implies nodes_context is present, so it's a subsystem command.
        # Subsystem command, e.g., SYSTem:ERRor. Needs ':' prefix.
        scpi_cmd_prefix = ":"
        
    # Filter out any empty parts that might have crept in (should be rare for valid commands)
    final_path_parts = [p for p in processed_path_parts if p]

    # Construct the base SCPI string template
    if not final_path_parts:
        # This case should ideally not be reached if cmd_info.path is always non-empty for a command.
        base_scpi_str = scpi_cmd_prefix 
    else:
        # If the (first part of the) command inherently starts with '*' (e.g. final_path_parts[0] = "*IDN"),
        # then scpi_cmd_prefix would have been set to "", so no double prefixing.
        # Otherwise, scpi_cmd_prefix ('*' or ':') is prepended.
        # All parts are joined by ':'.
        if final_path_parts[0].startswith("*"): # Already has a '*'
            base_scpi_str = ":".join(final_path_parts)
        else:
            base_scpi_str = scpi_cmd_prefix + ":".join(final_path_parts)
            
    cmd_dict['base_scpi_str_template'] = base_scpi_str
    # --- End of replacement block ---

    for syn_idx, syn_obj in enumerate(cmd_info.command_syntaxes):
        syn_info: Dict[str, Any] = {
            "name": syn_obj.name,
            "py_name": sanitize_enum_name(syn_obj.name).upper() if syn_obj.name else f"SYNTAX_{syn_idx}",
            "is_binary": bool(syn_obj.name and syn_obj.name.startswith("Block")),
            "params": [] 
        }
        if not is_query and syn_obj.parameters:
            for p_obj in syn_obj.parameters:
                syn_info["params"].append({"name": p_obj.name})
        cmd_dict['syntaxes_info'].append(syn_info)

    cmd_dict['overloads'] = []
    if not is_query and not cmd_dict['is_single_syntax']:
        overload_node_suffix_sig_parts = []
        if nodes_context:
            for node in nodes_context:
                if node.suffixes:
                    suffix_var = f"{node.mnemonic.lower()}_{node.suffixes.name}"
                    overload_node_suffix_sig_parts.append(f"{suffix_var}: int")

        for syn_obj in cmd_info.command_syntaxes:
            overload_sig_parts: List[str] = list(overload_node_suffix_sig_parts) 
            overload_sig_parts.append(f"syntax: {cmd_dict['syntax_enum_name']}.{sanitize_enum_name(syn_obj.name).upper()}")
            
            if syn_obj.parameters:
                for p_data in syn_obj.parameters:
                    p_types_list = get_parameter_types(p_data, global_defs_map)
                    overload_sig_parts.append(f"{p_data.name}: {parameter_types_as_string(p_types_list)}")
            cmd_dict['overloads'].append({"signature_parts": overload_sig_parts})
            
    return cmd_dict

def _prepare_node_for_template(
    node: Node,
    global_defs_map: Dict[str, GlobalDefinition],
    parent_nodes_ctx: List[Node] = None
) -> Dict[str, Any]:
    node_data: Dict[str, Any] = {
        "name": node.mnemonic, 
        "commands": [],
        "child_subsystems": []
    }
    current_nodes_context = (parent_nodes_ctx if parent_nodes_ctx else []) + [node]

    for cmd_info_obj in node.commands:
        if cmd_info_obj.has_query:
            node_data['commands'].append(
                _process_command_for_template(cmd_info_obj, True, global_defs_map, current_nodes_context)
            )
        if cmd_info_obj.has_write: 
            node_data['commands'].append(
                _process_command_for_template(cmd_info_obj, False, global_defs_map, current_nodes_context)
            )
    
    for child_node_obj in node.nodes:
        node_data['child_subsystems'].append(
            _prepare_node_for_template(child_node_obj, global_defs_map, current_nodes_context)
        )
    return node_data

def prepare_template_data(
    parsed_data: ParsedData,
    sdl_filename: str,
    supported_models: List[str]
) -> Dict[str, Any]:
    template_ctx: Dict[str, Any] = {}
    
    base_sdl_name = os.path.splitext(os.path.basename(sdl_filename))[0]
    template_ctx['main_class_name'] = f"Keysight{base_sdl_name}"
    template_ctx['sdl_filename_base'] = base_sdl_name
    template_ctx['supported_models'] = supported_models

    # template_ctx['validator_code'] = generate_validator_code()

    global_enums_list: List[Dict[str, Any]] = []
    processed_enum_names = set()
    for enum_def_orig in parsed_data.global_definitions.values():
        s_name = sanitize_enum_name(enum_def_orig.name)
        if s_name in processed_enum_names:
            continue 
        processed_enum_names.add(s_name)

        members = []
        for member in enum_def_orig.members:
            m_name = re.sub(r"[^a-zA-Z0-9_]", "_", member.mnemonic).upper()
            if not m_name: m_name = f"MEMBER_{member.value}" 
            if re.match(r"^\d", m_name): m_name = f"_{m_name}" 

            members.append({
                "name": m_name,
                "value": repr(member.value), 
                "description": member.description or ""
            })
        global_enums_list.append({
            "name": s_name,
            "original_name": enum_def_orig.name,
            "members": members
        })
    template_ctx['global_enums'] = sorted(global_enums_list, key=lambda x: x['name'])

    cmd_syntax_enums_list: List[Dict[str, Any]] = []
    seen_syntax_enum_names = set()

    def _collect_syntax_enums_recursive(target_node: Node):
        for cmd_info in target_node.commands:
            if len(cmd_info.command_syntaxes) > 1 and not cmd_info.has_query: 
                enum_name = f"{sanitize_enum_name('_'.join(cmd_info.path).upper())}Syntax"
                if enum_name not in seen_syntax_enum_names:
                    seen_syntax_enum_names.add(enum_name)
                    members = []
                    for syntax in cmd_info.command_syntaxes:
                        if syntax.name: 
                            member_py_name = sanitize_enum_name(syntax.name).upper()
                            members.append({"name": member_py_name, "value_str": syntax.name})
                    if members: 
                        cmd_syntax_enums_list.append({
                            "name": enum_name,
                            "command_path_str": ':'.join(cmd_info.path),
                            "members": members
                        })
        for child in target_node.nodes:
            _collect_syntax_enums_recursive(child)

    for cmd_info_direct in parsed_data.commands: 
         if len(cmd_info_direct.command_syntaxes) > 1 and not cmd_info_direct.has_query:
            enum_name = f"{sanitize_enum_name('_'.join(cmd_info_direct.path).upper())}Syntax"
            if enum_name not in seen_syntax_enum_names:
                seen_syntax_enum_names.add(enum_name)
                members = []
                for syntax in cmd_info_direct.command_syntaxes:
                    if syntax.name:
                        member_py_name = sanitize_enum_name(syntax.name).upper()
                        members.append({"name": member_py_name, "value_str": syntax.name})
                if members:
                    cmd_syntax_enums_list.append({
                        "name": enum_name,
                        "command_path_str": ':'.join(cmd_info_direct.path),
                        "members": members
                    })

    for subsystem in parsed_data.subsystems:
        _collect_syntax_enums_recursive(subsystem)
    template_ctx['command_syntax_enums'] = sorted(cmd_syntax_enums_list, key=lambda x: x['name'])
    
    template_ctx['binary_format_methods_code'] = generate_binary_format_methods_code()

    direct_cmds_list: List[Dict[str, Any]] = []
    for cmd_info in parsed_data.commands:
        if cmd_info.has_query:
            direct_cmds_list.append(
                _process_command_for_template(cmd_info, True, parsed_data.global_definitions)
            )
        if cmd_info.has_write: 
            direct_cmds_list.append(
                _process_command_for_template(cmd_info, False, parsed_data.global_definitions)
            )
    template_ctx['direct_commands'] = direct_cmds_list
    
    subsystems_list: List[Dict[str, Any]] = []
    for subsystem_node in parsed_data.subsystems:
        subsystems_list.append(
            _prepare_node_for_template(subsystem_node, parsed_data.global_definitions, [])
        )
    template_ctx['subsystems'] = subsystems_list
    
    return template_ctx

def generate_code(parsed_data: ParsedData, sdl_file_path: str, supported_mdls: List[str], template_dir='templates', output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True,
        extensions=['jinja2.ext.do'] 
    )
    template = env.get_template('class_template.j2')

    print("Preparing data for template...")
    template_input_data = prepare_template_data(parsed_data, sdl_file_path, supported_mdls)
    
    print("Rendering template...")
    class_code = template.render(template_input_data)
    
    main_class_name_val = template_input_data['main_class_name']
    output_filename_base = main_class_name_val.lower()
    # Consistent naming with agilent_class_generator.py (e.g. keysight33500b.py instead of keysightkeysight33500b.py)
    if output_filename_base.startswith("keysight") and template_input_data['sdl_filename_base'].lower().startswith("keysight"):
         output_filename_base = template_input_data['sdl_filename_base'].lower() # Use the sanitized sdl name directly if it already has keysight
    elif not output_filename_base.startswith("keysight"):
        output_filename_base = f"keysight{output_filename_base}"


    class_file = os.path.join(output_dir, f"{output_filename_base}.py")
    
    print(f"Writing generated code to {class_file}...")
    with open(class_file, 'w', encoding='utf-8') as f:
            f.write(class_code)
    print(f"Successfully generated {class_file}")



if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate Python classes from Agilent SDL file')
    parser.add_argument('--input-file', help='Path to the input SDL file')
    parser.add_argument('--output-dir', help='Directory where the output Python file will be stored (optional)')
    parser.add_argument('--idf-file', help='Path to the IDF file containing supported models information')
    
    # Parse arguments
    args = parser.parse_args()  

    sdl_file = args.input_file
    if not sdl_file:
        raise ValueError("Input SDL file is required")

    # Extract supported models if IDF file is provided
    supported_models = []
    if args.idf_file:
        supported_models = extract_supported_models(args.idf_file)
        if supported_models:
            print(f"Found {len(supported_models)} supported models: {', '.join(supported_models)}")
    
    output_path = args.output_dir
    if not output_path:
        raise ValueError("Output directory is required")


    print(f"Parsing SDL file: {sdl_file}...")
    parsed_sdl_data = parse_sdl_file(sdl_file)
    print("SDL file parsed.")

    generate_code(
        parsed_data=parsed_sdl_data,
        sdl_file_path=sdl_file,
        supported_mdls=supported_models,
        template_dir=os.path.join(os.path.dirname(__file__), 'templates'), 
        output_dir=output_path
    )

    generate_info_file()

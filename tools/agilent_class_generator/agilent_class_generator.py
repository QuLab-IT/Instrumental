from instrumental.parse_modules import generate_info_file
from parse_agilent_sdl import (
    parse_sdl_file,
    ParsedData,
    CommandInfo,
    ParameterData,
    ResponseData,
    CommandSyntax,
    ParameterType,
    EnumMember,
    GlobalDefinitions,
    Node,
    NodeSuffix,
    extract_supported_models,
)
from typing import Dict, List, Optional, Union, Any
import re
import numpy as np
from utils import sanitize_enum_name
import argparse
import os
import xml.etree.ElementTree as ET

def generate_enum_class(enum_name: str, members: List[EnumMember]) -> str:
    """
    Generate a Python enum class from enum data.

    Args:
        enum_name (str): The name of the enum
        members (List[EnumMember]): List of enum members

    Returns:
        str: The generated Python enum class code
    """
    class_name = sanitize_enum_name(enum_name)

    # Generate the class header
    code = f"class {class_name}(Enum):\n"
    code += '    """\n'
    code += f"    Enum for {enum_name}\n"
    code += '    """\n\n'

    # Add each member
    for member in members:
        mnemonic = member.mnemonic
        value = member.value
        description = member.description

        # Create a valid Python identifier from the mnemonic
        member_name = re.sub(r"[^a-zA-Z0-9]", "_", mnemonic).upper()

        # Add the member with its value and description
        code += f"    {member_name} = {value}\n"
        if description:
            code += f"    # {description}\n"
        if member.aliases:
            code += f"    # Aliases: {member.aliases}\n"
        code += "\n"

    return code


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
    docstring = '        """\n'
    docstring += f"        {cmd_info.synopsis}\n\n"

    # Document parameters based on command type and available syntaxes
    has_parameters = is_write and cmd_info.command_syntaxes
    has_suffixes = nodes and any(node.suffixes for node in nodes)
    
    if has_parameters or has_suffixes:
        docstring += "        Args:\n"
        
        # Document node suffixes first
        if has_suffixes:
            for node in nodes:
                if node.suffixes:
                    suffix_name = f"{node.mnemonic.lower()}_{node.suffixes.name}"
                    docstring += f"            {suffix_name} (int): {node.suffixes.description}"
                    if node.suffixes.min_value is not None and node.suffixes.max_value is not None:
                        docstring += f" (Range: {node.suffixes.min_value}-{node.suffixes.max_value})"
                    docstring += "\n"

        # Document syntax parameter if multiple syntaxes
        if len(cmd_info.command_syntaxes) > 1:
            enum_name = f"{sanitize_enum_name('_'.join(cmd_info.path)).upper()}Syntax"
            docstring += f"            syntax ({enum_name}): The syntax variant to use for this command\n"

        # Document command parameters for each syntax
        if has_parameters:
            for syntax in cmd_info.command_syntaxes:
                if len(cmd_info.command_syntaxes) > 1:
                    docstring += f"\n            For syntax {syntax.name}:\n"
                if syntax.parameters:
                    for param in syntax.parameters:
                        param_desc = f"{param.description}"
                        if param.repeat:
                            param_desc += f" (Repeatable: {param.repeat})"
                        if len(cmd_info.command_syntaxes) > 1:
                            docstring += f"                {param.name} ({(param.to_python_type())}): {param_desc}\n"
                        else:
                            docstring += f"            {param.name} ({param.to_python_type()}): {param_desc}\n"

    if not is_write and cmd_info.responses:
        docstring += "\n        Returns:\n"
        for response in cmd_info.responses:
            docstring += f"            {response.to_python_type()}: {response.description}\n"

    docstring += '        """\n'
    return docstring


def get_parameter_type(param: ParameterData) -> str:
    """
    Get the Python type annotation for a parameter based on its types.
    If there are non-enum parameter types, they will be added as optional types
    using the semantic type.

    Args:
        param (ParameterData): Parameter information dataclass

    Returns:
        str: The Python type annotation
    """
    types = []

    # Add parameter types if present
    if param.parameter_types:
        for pt in param.parameter_types:
            if pt.enum_ref:
                type = sanitize_enum_name(pt.enum_ref)
            elif pt.type_name:
                # For other types, use the Python type mapping
                type = param.to_python_type()
            if type not in types:
                types.append(type)

    # If no types were found, return Any
    if not types:
        return "Any"

    # If only one type, return it directly
    if len(types) == 1:
        return types[0]

    # If multiple types, return a Union
    return f"Union[{', '.join(types)}]"


def get_response_type(response: ResponseData) -> str:
    """
    Get the Python type annotation for a parameter based on its types.
    If there are non-enum parameter types, they will be added as optional types
    using the semantic type.

    Args:
        param (ParameterData): Parameter information dataclass

    Returns:
        str: The Python type annotation
    """
    types = []

    # Add parameter types if present
    if response.response_types:
        for response_type in response.response_types:
            if response_type.enum_ref:
                type = sanitize_enum_name(response_type.enum_ref)
            elif response_type.type_name:
                # For other types, use the Python type mapping
                type = response.to_python_type()
            if type not in types:
                types.append(type)

    # If no types were found, return Any
    if not types:
        return "Any"

    # If only one type, return it directly
    if len(types) == 1:
        return types[0]

    # If multiple types, return a Union
    return f"Union[{', '.join(types)}]"

def get_method_name(command_info: CommandInfo, is_query: bool, has_parameters: bool) -> str:
    base_name = "_".join(command_info.path).lower()
    if is_query:
        method_name = f"get_{base_name}"
    else:
        # For write commands
        if has_parameters:
            method_name = f"set_{base_name}"
        else:
            method_name = base_name
    return method_name

def generate_binary_format_methods() -> str:
    """
    Generate methods for handling binary data formats.
    
    Returns:
        str: The generated methods code
    """
    return """
    def _set_binary_format(self, format_name: str) -> None:
        \"\"\"Set the binary data format for subsequent commands.
        
        Args:
            format_name: The format name (e.g., 'BlockInt16', 'BlockReal32')
        \"\"\"
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
        \"\"\"Prepare binary data according to the specified format.
        
        Args:
            data: The data to convert
            format_name: The format name (e.g., 'BlockInt16', 'BlockReal32')
            
        Returns:
            bytes: The prepared binary data
        \"\"\"
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
        \"\"\"Write a command with binary data.
        
        Args:
            cmd: The SCPI command string
            data: The binary data to write
            format_name: The format name (e.g., 'BlockInt16', 'BlockReal32')
        \"\"\"
        # Set the binary format
        self._set_binary_format(format_name)
        
        # Prepare the binary data
        binary_data = self._prepare_binary_data(data, format_name)
        
        # Write the command and data
        self._rsrc.write_binary_values(cmd, binary_data)
"""

def generate_command_method(
    cmd_info: CommandInfo,
    is_query: bool,
    nodes: List[Node] = None,
) -> str:
    """
    Generate a Python method for a SCPI command.

    Args:
        cmd_info: Command information dataclass
        is_query: Whether this is a query method
        nodes: List of nodes that might have suffixes

    Returns:
        str: The generated method code
    """
    # Generate method signature
    has_parameters = any(syntax.parameters for syntax in cmd_info.command_syntaxes)
    method_name = get_method_name(cmd_info, is_query, has_parameters)
    params = []
    extra_params = []
    # Add syntax parameter if multiple syntaxes exist
    if len(cmd_info.command_syntaxes) > 1:
        enum_name = f"{sanitize_enum_name('_'.join(cmd_info.path).upper())}Syntax"
        extra_params.append(f"syntax: {enum_name}")

    path_parts = []
    separator = ":"
    prefix = ""
    if nodes:
        prefix = separator
        for node in nodes:
            part = node.mnemonic
            if node.suffixes:
                suffix_variable_name = f"{node.mnemonic.lower()}_{node.suffixes.name}"
                extra_params.append(f"{suffix_variable_name}: int = 1")  # All suffixes are integers
                part += f"{{{suffix_variable_name}}}"
            path_parts.append(part)
    else:
        prefix = "*"
        path_parts.extend(cmd_info.path)
    base_syntax = prefix + (separator.join(path_parts) if len(path_parts) > 1 else path_parts[0])


    # Add command parameters based on command type
    if not is_query and has_parameters and cmd_info.command_syntaxes:
        if len(cmd_info.command_syntaxes) > 1:
            # For multiple syntaxes, find common parameters and add them
            common_param_names = set(param.name for param in cmd_info.command_syntaxes[0].parameters)
            for syntax in cmd_info.command_syntaxes[1:]:
                common_param_names &= set(param.name for param in syntax.parameters)
            
            # Add common parameters (only once)
            added_params = set()
            for syntax in cmd_info.command_syntaxes:
                for param in syntax.parameters:
                    if param.name in common_param_names and param.name not in added_params:
                        param_type = get_parameter_type(param)
                        param_name = param.name
                        params.append(f"{param_name}: {param_type}")
                        added_params.add(param.name)
            
            # Add unified data parameter for syntax-specific parameters
            params.append("data: Union[int, Any]")
        else:
            # Single syntax case - add all parameters
            for param in cmd_info.command_syntaxes[0].parameters:
                param_type = get_parameter_type(param)
                param_name = param.name
                params.append(f"{param_name}: {param_type}")

    method_signature = f"    def {method_name}(self"
    params.extend(extra_params)
    if params:
        method_signature += f", {', '.join(params)}"
    method_signature += ")"

    # Generate return type annotation
    if is_query and cmd_info.responses:
        response_type = get_response_type(cmd_info.responses[0])
        method_signature += f" -> {response_type}"

    method_signature += ":\n"

    # Generate method body
    method_body = generate_method_docstring(cmd_info, is_write=not is_query, nodes=nodes)

    # Generate command string
    if len(cmd_info.command_syntaxes) > 1:
        # Handle multiple syntaxes with a match statement
        method_body += "        # Get parameters based on selected syntax\n"
        method_body += "        match syntax:\n"
        for syntax in cmd_info.command_syntaxes:
            syntax_name = re.sub(r"[^a-zA-Z0-9]", "_", syntax.name).upper()
            method_body += f"            case {enum_name}.{syntax_name}:\n"
            
            # Add type validation for ASCII syntax
            if syntax_name == "ASCII":
                method_body += "                if not isinstance(data, int):\n"
                method_body += '                    raise TypeError("For ASCII syntax, data must be an integer")\n'
            
            method_body += f'                cmd = f"{base_syntax}'  # Note the f-string
            if syntax.parameters:
                method_body += " "
                param_parts = []
                # First add common parameters
                for param in syntax.parameters:
                    if param.name in common_param_names:
                        param_parts.append(f"{{{param.name}}}")
                # Then add the data parameter
                param_parts.append("{data}")
                method_body += ", ".join(param_parts)
            if is_query:
                method_body += '?"\n'
            else:
                method_body += '"\n'
    else:
        # Simple case with single syntax
        method_body += "        cmd = f"  # Always use f-string when we have suffixes
        method_body += f'"{base_syntax}'
        if (
            not is_query
            and cmd_info.command_syntaxes
            and cmd_info.command_syntaxes[0].parameters
        ):
            method_body += " "
            param_parts = []
            for param in cmd_info.command_syntaxes[0].parameters:
                param_parts.append(f"{{{param.name}}}")
            method_body += ", ".join(param_parts)
        if is_query:
            method_body += '?"\n'
        else:
            method_body += '"\n'

    # Generate command execution
    if is_query:
        method_body += "        response = self._rsrc.query(cmd)\n"
        if cmd_info.responses:
            response_type = cmd_info.responses[0].to_python_type_converter()
            method_body += f"        return {response_type}(response)\n"
    else:  # has_write
        # Check if this is a binary data command
        is_binary = any(syntax.name.startswith('Block') for syntax in cmd_info.command_syntaxes)
        if is_binary:
            method_body += "        # Handle binary data\n"
            method_body += "        if isinstance(data, (list, tuple, np.ndarray)):\n"
            method_body += "            self._write_binary_data(cmd, data, syntax.name)\n"
            method_body += "        else:\n"
            method_body += "            self._rsrc.write(cmd)\n"
        else:
            method_body += "        self._rsrc.write(cmd)\n"

    return method_signature + method_body + "\n"

def generate_overload_methods(
    cmd_info: CommandInfo, 
    parent_nodes: List[Node] = None
) -> str:
    """
    Generate overload methods for a SCPI command.

    Args:
        cmd_info: Command information dataclass
        cmd_path: List of command path components
        method_name: The name of the method to generate
        node_suffixes: List of NodeSuffix objects for this command's path

    Returns:
        str: The generated overload method code
    """
    has_parameters = any(syntax.parameters for syntax in cmd_info.command_syntaxes)
    method_name = get_method_name(cmd_info, is_query=False, has_parameters=has_parameters)
    enum_name = f"{sanitize_enum_name('_'.join(cmd_info.path).upper())}Syntax"
    overload_code = ""
    
    for syntax in cmd_info.command_syntaxes:
        syntax_name = re.sub(r"[^a-zA-Z0-9]", "_", syntax.name).upper()
        overload_code += f"    @overload\n"
        overload_code += f"    def {method_name}(self"
        
        # Add suffix parameters first
        if parent_nodes:
            for node in parent_nodes:
                if node.suffixes:
                    overload_code += f", {node.mnemonic.lower()}_{node.suffixes.name}: int"
        
        # Add syntax parameter
        overload_code += f", syntax: {enum_name}.{syntax_name}"
        
        # Add command parameters
        if syntax.parameters:
            for param in syntax.parameters:
                param_type = get_parameter_type(param)
                overload_code += f", {param.name}: {param_type}"
        
        overload_code += ") -> None: ...\n\n"
    
    return overload_code

def generate_node_methods(node: Node, parent_path: List[str] = [], parent_nodes: List[Node] = None) -> str:
    """
    Generate methods for a SCPI node.
    
    Args:
        node: The node information
        parent_path: The path of parent nodes
        parent_suffixes: List of NodeSuffix objects from parent nodes
        
    Returns:
        str: The generated methods code
    """
    current_path = parent_path + [node.mnemonic]
    
    # Collect all suffixes (parent suffixes + this node's suffix if any)
    current_nodes = list(parent_nodes) if parent_nodes else []
    if node:
        current_nodes.append(node)

    # Track seen method names to avoid duplicates
    seen_methods = set()
    class_code = ""

    # Generate methods for each command
    for cmd in node.commands:
        cmd_path = cmd.path
        base_name = cmd_path[-1].lower()

        # Skip if we've already generated this method
        if base_name in seen_methods:
            continue
        seen_methods.add(base_name)

        if cmd.has_query:
            # For query commands
            class_code += generate_command_method(cmd, True, current_nodes)
        if cmd.has_write:
            # Generate overloads for write commands with multiple syntaxes
            if len(cmd.command_syntaxes) > 1:
                class_code += generate_overload_methods(cmd, current_nodes)

            # Generate the actual implementation
            class_code += generate_command_method(cmd, False, current_nodes)

    # Generate child node methods
    for child in node.nodes:
        class_code += generate_node_methods(child, current_path, current_nodes)

    return class_code


def generate_subsystem_methods(subsystem_info: Node) -> str:
    """
    Generate a Python class for a SCPI subsystem.
    
    Args:
        subsystem_info: The subsystem information
        
    Returns:
        str: The generated class code
    """
    # Track seen method names to avoid duplicates
    class_code = ""
    # Generate methods for each command
    for cmd in subsystem_info.commands:
        if cmd.has_query:
            # For query commands
            class_code += generate_command_method(cmd, True)
        if cmd.has_write:
            # Generate overloads for write commands with multiple syntaxes
            if len(cmd.command_syntaxes) > 1:
                class_code += generate_overload_methods(cmd)

            # Generate the actual implementation
            class_code += generate_command_method(cmd, False)

    # Generate child node instances
    mnemonic = subsystem_info.mnemonic
    for node in subsystem_info.nodes:
        class_code += generate_node_methods(node, [mnemonic], [subsystem_info])

    return class_code


def generate_enums_file(parsed_data: ParsedData) -> List[str]:
    """
    Generate Python enum classes from the SDL file.

    Args:
        file_path (str): Path to the SDL file
        output_file (str): Path to the output Python file

    Returns:
        List[str]: List of generated content lines
    """
    global_defs = parsed_data.global_definitions

    # Generate the content
    content = [
        "from enum import Enum",
        "from typing import Any, Union, overload",
        "import pyvisa",
        "import numpy as np",
        "",
        "# Generated SCPI enums from SDL file",
        "# This file is auto-generated. Do not edit manually.",
        "",
    ]

    # Add each enum class
    for enum_name, enum_data in global_defs.items():
        content.append(generate_enum_class(enum_name, enum_data.members))
        content.append("")  # Add blank line between classes

    print(f"Generated {len(global_defs)} enum classes")
    return content

def generate_command_syntax_enum_name(cmd_path: List[str]) -> str:
    """
    Generate a Python enum name for command syntaxes.
    """
    return f"{sanitize_enum_name('_'.join(cmd_path))}Syntax"

def generate_command_syntax_enum(
    cmd_info: CommandInfo, cmd_path: List[str]
) -> Optional[str]:
    """
    Generate a Python enum class for command syntaxes if the command has multiple syntaxes.

    Args:
        cmd_info (CommandInfo): Command information dataclass
        cmd_path (List[str]): List of command path components

    Returns:
        Optional[str]: The generated enum class code if multiple syntaxes exist, None otherwise
    """
    if not cmd_info.command_syntaxes or len(cmd_info.command_syntaxes) <= 1:
        return None

    # Create enum name from command path
    enum_name = generate_command_syntax_enum_name(cmd_path)

    # Generate the class header
    code = f"class {enum_name}(Enum):\n"
    code += '    """\n'
    code += f"    Enum for command syntaxes of {':'.join(cmd_path)}\n"
    code += '    """\n\n'

    # Add each syntax as an enum member
    for syntax in cmd_info.command_syntaxes:
        syntax_name = syntax.name
        if not syntax_name:
            continue

        # Create a valid Python identifier from the syntax name
        member_name = re.sub(r"[^a-zA-Z0-9]", "_", syntax_name).upper()

        # Add the member with its value
        code += f'    {member_name} = "{syntax_name}"\n'

        # Add parameter information as comments
        if syntax.parameters:
            code += "    # Parameters:\n"
            for param in syntax.parameters:
                code += f"    #   - {param.name} ({param.semantic_type})\n"
                code += f"    #     Description: {param.description}\n"
                if param.repeat:
                    code += f"    #     Repeat: {param.repeat}\n"
        code += "\n"

    return code


def generate_command_syntaxes_file(parsed_data: ParsedData) -> List[str]:
    """
    Generate Python enum classes for command syntaxes.

    Args:
        file_path (str): Path to the SDL file

    Returns:
        List[str]: List of generated content lines
    """

    # Generate the content
    content = [
        "",
        "# Generated SCPI command syntax enums",
        "# These enums represent different syntax variants for commands that support multiple formats",
        "",
    ]

    # Track seen enum names to avoid duplicates
    seen_enum_names = set()

    def process_node(node: Node) -> None:
        """Recursively process a node and its children to generate syntax enums."""
        # Process commands in this node
        for cmd in node.commands:
            enum_code = generate_command_syntax_enum(cmd, cmd.path)
            if enum_code:
                enum_name = enum_code.split("\n")[0].split("(")[0].split()[-1]
                if enum_name not in seen_enum_names:
                    seen_enum_names.add(enum_name)
                    content.append(enum_code)
                    content.append("")  # Add blank line between classes

        # Process child nodes
        for child in node.nodes:
            process_node(child)

    # Process each subsystem and its nodes
    for subsystem in parsed_data.subsystems:
        process_node(subsystem)

    print(f"Generated {len(seen_enum_names)} command syntax enum classes")
    return content


def generate_subsystems_methods(subsystems: List[Node]) -> List[str]:
    """
    Generate Python classes for all SCPI subsystems.

    Args:
        file_path (str): Path to the SDL file

    Returns:
        List[str]: List of generated content lines
    """

    # Generate the content
    content = [
        "",
        "   # Generated SCPI subsystem methods",
        "   # These methods provide a Pythonic interface to SCPI commands",
        "",
    ]

    # Add each subsystem class
    for subsystem in subsystems:
        content.append(generate_node_methods(subsystem))
        content.append("")  # Add blank line between classes

    print(f"Generated {len(subsystems)} subsystem methods")
    return content

def generate_main_class_name(sdl_filename: str) -> str:
    """
    Generate the main class name from the SDL filename.
    """
    return f"Keysight{os.path.splitext(os.path.basename(sdl_filename))[0]}"

def generate_main_class(parsed_data: ParsedData, supported_models: List[str], sdl_filename: str) -> str:
    """
    Generate the main class that includes all commands and subsystem instances.
    
    Args:
        parsed_data: The parsed SDL data
        supported_models: List of supported model numbers
        sdl_filename: The name of the SDL file being parsed
        
    Returns:
        str: The generated class code
    """
    class_name = generate_main_class_name(sdl_filename)

    # Generate the content
    content = [
        "",
        f"# Main {class_name} class",
        "# This class provides access to all SCPI commands and subsystems",
        "",
        "from instrumental.drivers import VisaMixin",
        "from instrumental.drivers.funcgenerators import FunctionGenerator",
        "import numpy as np",
        "from numpy.typing import NDArray",
        "",
        f"class {class_name}(FunctionGenerator, VisaMixin):",
        f'    """Main class for controlling the Keysight {sdl_filename.split(".")[0]} function generators."""',
        "    _INST_PARAMS_ = ['visa_address']",
        f"    _INST_VISA_INFO_ = ('Agilent Technologies', {supported_models})",
        "",
        "    def _initialize(self):",
        "        self._rsrc.timeout = 2000  # 2 second timeout",
        "        self._rsrc.write_termination = '\\n'",
        "        self._rsrc.read_termination = '\\n'\n",
    ]

    # Add binary format handling methods
    content.append(generate_binary_format_methods())

    content.append("")  # Add blank line after subsystem instances

    # Add direct command methods
    for cmd in parsed_data.commands:
        if cmd.has_query:
            # For query-only commands
            content.append(generate_command_method(cmd, True))
        if cmd.has_write:
            # Generate overloads for write commands with multiple syntaxes
            if len(cmd.command_syntaxes) > 1:
                content.append(generate_overload_methods(cmd))
                # Generate the actual implementation
            content.append(generate_command_method(
                cmd, False
            ))

    content.extend(generate_subsystems_methods(parsed_data.subsystems))
    return "\n".join(content)


def generate_test_file(parsed_data: ParsedData, supported_models: List[str], sdl_filename: str) -> str:
    """
    Generate a test file for the generated class.
    
    Args:
        parsed_data: The parsed SDL data
        supported_models: List of supported model numbers
        sdl_filename: The name of the SDL file being parsed
        
    Returns:
        str: The generated test file content
    """
    class_name = generate_main_class_name(sdl_filename)

    # Track all enum classes we need to import
    enum_imports = set()
    
    def collect_enum_imports(cmd: CommandInfo) -> None:
        """Collect all enum classes needed for a command."""
        # Collect parameter enum types
        if cmd.command_syntaxes:
            syntax = cmd.command_syntaxes[0]
            if syntax.parameters:
                for param in syntax.parameters:
                    if param.parameter_types:
                        for pt in param.parameter_types:
                            if pt.enum_ref:
                                enum_imports.add(sanitize_enum_name(pt.enum_ref))
        
        # Collect command syntax enum if multiple syntaxes exist
        if len(cmd.command_syntaxes) > 1:
            enum_name = generate_command_syntax_enum_name(cmd.path)
            print(f"Adding syntax enum: {enum_name} for command path: {cmd.path}")  # Debug print
            enum_imports.add(enum_name)
    
    # Collect enum imports from all commands
    for cmd in parsed_data.commands:
        collect_enum_imports(cmd)
    
    # Collect enum imports from all subsystems
    def collect_subsystem_enum_imports(node: Node) -> None:
        for cmd in node.commands:
            collect_enum_imports(cmd)
        for child in node.nodes:
            collect_subsystem_enum_imports(child)
    
    for subsystem in parsed_data.subsystems:
        collect_subsystem_enum_imports(subsystem)
    
    # Generate the content with imports
    content = [
        "import pytest",
        "import numpy as np",
        "import os",
        "",
        f"# Generated test file for {class_name} class",
        "# This file is auto-generated. Do not edit manually.",
        "",
        "# Add the parent directory to the Python path to import the driver",
        "import sys",
        "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))",
        "",
        "# Import all required enum classes",
        f"from instrumental.drivers.funcgenerators.{class_name.lower()} import (",
        f"    {class_name},",
    ]
    
    # Add enum imports
    if enum_imports:
        content.append("    " + ",\n    ".join(sorted(enum_imports)))
    content.append(")")
    content.extend([
        "",
        f"class Test{class_name}:",
        "",
    ])

    def get_test_arguments(cmd: CommandInfo, nodes: List[Node] = None) -> str:
        """Generate test arguments for a command based on its parameters and node suffixes."""
        args = []
        seen_params = set()  # Track seen parameter names
        
        # Add node suffix arguments if they exist
        if nodes:
            for node in nodes:
                if node.suffixes:
                    suffix_name = f"{node.mnemonic.lower()}_{node.suffixes.name}"
                    if suffix_name not in seen_params:
                        args.append(f"{suffix_name}=1")
                        seen_params.add(suffix_name)
        
        # Add command parameters based on syntax
        if cmd.command_syntaxes:
            # For multiple syntaxes, use the first one as default
            syntax = cmd.command_syntaxes[0]
            if syntax.parameters:
                for param in syntax.parameters:
                    # Skip if we've already added this parameter
                    if param.name in seen_params:
                        continue
                        
                    # Generate appropriate test value based on parameter type
                    if param.parameter_types:
                        # Use the first parameter type to determine the value
                        pt = param.parameter_types[0]
                        if pt.enum_ref:
                            # For enum types, get all possible values from the parsed data
                            enum_name = sanitize_enum_name(pt.enum_ref)
                            # Get enum members from the parsed data
                            enum_members = parsed_data.global_definitions[pt.enum_ref].members
                            # Format enum values as a list
                            enum_values = [f"{enum_name}.{member.mnemonic}" for member in enum_members]
                            args.append(f"{param.name}={enum_values}")
                        elif pt.type_name:
                            # For numeric types, use a reasonable default
                            if pt.type_name in ['NR1', 'NR2', 'NR3']:
                                args.append(f"{param.name}=1.0")
                            elif pt.type_name == 'Boolean':
                                args.append(f"{param.name}=True")
                            else:
                                args.append(f"{param.name}=1")
                        seen_params.add(param.name)
        
        return ", ".join(args)

    # Add test cases for direct commands
    for cmd in parsed_data.commands:
        if cmd.has_query:
            # Generate test for query command
            method_name = get_method_name(cmd, is_query=True, has_parameters=False)
            args = get_test_arguments(cmd)
            content.extend([
                f"    def test_{method_name}(self, inst: {class_name}):",
                f"        # Test {cmd.synopsis}",
                "",
                f"        # Call the method",
                f"        result = inst.{method_name}({args})",
                "",
                "        # Verify the response is not None",
                "        assert result is not None",
                "",
            ])

        if cmd.has_write:
            # Generate test for write command
            has_parameters = any(syntax.parameters for syntax in cmd.command_syntaxes)
            method_name = get_method_name(cmd, is_query=False, has_parameters=has_parameters)
            
            # Generate test cases for each syntax if multiple exist
            if len(cmd.command_syntaxes) > 1:
                enum_name = generate_command_syntax_enum_name(cmd.path)
                for syntax in cmd.command_syntaxes:
                    syntax_name = re.sub(r"[^a-zA-Z0-9]", "_", syntax.name).upper()
                    args = get_test_arguments(cmd)
                    if args:
                        args = f"{args}, "
                    args += f"syntax={enum_name}.{syntax_name}"
                    
                    # For each enum parameter, generate a test case for each value
                    for param in syntax.parameters:
                        if param.parameter_types and param.parameter_types[0].enum_ref:
                            enum_name = sanitize_enum_name(param.parameter_types[0].enum_ref)
                            enum_members = parsed_data.global_definitions[param.parameter_types[0].enum_ref].members
                            for member in enum_members:
                                test_args = args.replace(f"{param.name}={enum_name}.{enum_members}", 
                                                       f"{param.name}={enum_name}.{member.mnemonic}")
                                content.extend([
                                    f"    def test_{method_name}_{syntax_name.lower()}_{member.mnemonic.lower()}(self, inst: {class_name}):",
                                    f"        # Test {cmd.synopsis} with {syntax.name} syntax and {member.mnemonic} value",
                                    "",
                                    f"        # Call the method with {syntax.name} syntax and {member.mnemonic} value",
                                    f"        inst.{method_name}({test_args})",
                                    "",
                                    "        # Verify the command was executed without errors",
                                    "        # Note: We can't verify the exact command sent as it depends on the parameters",
                                    "",
                                ])
                        else:
                            content.extend([
                                f"    def test_{method_name}_{syntax_name.lower()}(self, inst: {class_name}):",
                                f"        # Test {cmd.synopsis} with {syntax.name} syntax",
                                "",
                                f"        # Call the method with {syntax.name} syntax",
                                f"        inst.{method_name}({args})",
                                "",
                                "        # Verify the command was executed without errors",
                                "        # Note: We can't verify the exact command sent as it depends on the parameters",
                                "",
                            ])
            else:
                # Single syntax case
                args = get_test_arguments(cmd)
                # For each enum parameter, generate a test case for each value
                for param in cmd.command_syntaxes[0].parameters:
                    if param.parameter_types and param.parameter_types[0].enum_ref:
                        enum_name = sanitize_enum_name(param.parameter_types[0].enum_ref)
                        enum_members = parsed_data.global_definitions[param.parameter_types[0].enum_ref].members
                        for member in enum_members:
                            test_args = args.replace(f"{param.name}={enum_name}.{enum_members}", 
                                                   f"{param.name}={enum_name}.{member.mnemonic}")
                            content.extend([
                                f"    def test_{method_name}_{member.mnemonic.lower()}(self, inst: {class_name}):",
                                f"        # Test {cmd.synopsis} with {member.mnemonic} value",
                                "",
                                f"        # Call the method with {member.mnemonic} value",
                                f"        inst.{method_name}({test_args})",
                                "",
                                "        # Verify the command was executed without errors",
                                "        # Note: We can't verify the exact command sent as it depends on the parameters",
                                "",
                            ])
                    else:
                        content.extend([
                            f"    def test_{method_name}(self, inst: {class_name}):",
                            f"        # Test {cmd.synopsis}",
                            "",
                            "        # Call the method",
                            f"        inst.{method_name}({args})",
                            "",
                            "        # Verify the command was executed without errors",
                            "        # Note: We can't verify the exact command sent as it depends on the parameters",
                            "",
                        ])

    # Add test cases for subsystem methods
    def generate_subsystem_tests(node: Node, parent_path: List[str] = None) -> List[str]:
        tests = []
        current_path = parent_path + [node.mnemonic] if parent_path else [node.mnemonic]
        
        # Generate tests for commands in this node
        for cmd in node.commands:
            if cmd.has_query:
                method_name = get_method_name(cmd, is_query=True, has_parameters=False)
                args = get_test_arguments(cmd, [node])
                tests.extend([
                    f"    def test_{method_name}(self, inst: {class_name}):",
                    f"        # Test {cmd.synopsis}",
                    "",
                    f"        # Call the method",
                    f"        result = inst.{method_name}({args})",
                    "",
                    "        # Verify the response is not None",
                    "        assert result is not None",
                    "",
                ])

            if cmd.has_write:
                has_parameters = any(syntax.parameters for syntax in cmd.command_syntaxes)
                method_name = get_method_name(cmd, is_query=False, has_parameters=has_parameters)
                
                if len(cmd.command_syntaxes) > 1:
                    enum_name = generate_command_syntax_enum_name(cmd.path)
                    for syntax in cmd.command_syntaxes:
                        syntax_name = re.sub(r"[^a-zA-Z0-9]", "_", syntax.name).upper()
                        args = get_test_arguments(cmd, [node])
                        if args:
                            args = f"{args}, "
                        args += f"syntax={enum_name}.{syntax_name}"
                        
                        # For each enum parameter, generate a test case for each value
                        for param in syntax.parameters:
                            if param.parameter_types and param.parameter_types[0].enum_ref:
                                enum_name = sanitize_enum_name(param.parameter_types[0].enum_ref)
                                enum_members = parsed_data.global_definitions[param.parameter_types[0].enum_ref].members
                                for member in enum_members:
                                    test_args = args.replace(f"{param.name}={enum_name}.{enum_members}", 
                                                           f"{param.name}={enum_name}.{member.mnemonic}")
                                    tests.extend([
                                        f"    def test_{method_name}_{syntax_name.lower()}_{member.mnemonic.lower()}(self, inst: {class_name}):",
                                        f"        # Test {cmd.synopsis} with {syntax.name} syntax and {member.mnemonic} value",
                                        "",
                                        f"        # Call the method with {syntax.name} syntax and {member.mnemonic} value",
                                        f"        inst.{method_name}({test_args})",
                                        "",
                                        "        # Verify the command was executed without errors",
                                        "        # Note: We can't verify the exact command sent as it depends on the parameters",
                                        "",
                                    ])
                            else:
                                tests.extend([
                                    f"    def test_{method_name}_{syntax_name.lower()}(self, inst: {class_name}):",
                                    f"        # Test {cmd.synopsis} with {syntax.name} syntax",
                                    "",
                                    f"        # Call the method with {syntax.name} syntax",
                                    f"        inst.{method_name}({args})",
                                    "",
                                    "        # Verify the command was executed without errors",
                                    "        # Note: We can't verify the exact command sent as it depends on the parameters",
                                    "",
                                ])
                else:
                    args = get_test_arguments(cmd, [node])
                    tests.extend([
                        f"    def test_{method_name}(self, inst: {class_name}):",
                        f"        # Test {cmd.synopsis}",
                        "",
                        "        # Call the method",
                        f"        inst.{method_name}({args})",
                        "",
                        "        # Verify the command was executed without errors",
                        "        # Note: We can't verify the exact command sent as it depends on the parameters",
                        "",
                    ])
        
        # Generate tests for child nodes
        for child in node.nodes:
            tests.extend(generate_subsystem_tests(child, current_path))
        
        return tests

    # Add tests for all subsystems
    for subsystem in parsed_data.subsystems:
        content.extend(generate_subsystem_tests(subsystem))

    return "\n".join(content)


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate Python classes from Agilent SDL file')
    parser.add_argument('input_file', help='Path to the input SDL file')
    parser.add_argument('--output-dir', help='Directory where the output Python file will be stored (optional)')
    parser.add_argument('--idf-file', help='Path to the IDF file containing supported models information')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Extract supported models if IDF file is provided
    supported_models = []
    if args.idf_file:
        supported_models = extract_supported_models(args.idf_file)
        if supported_models:
            print(f"Found {len(supported_models)} supported models: {', '.join(supported_models)}")
    
    # Parse the SDL file
    parsed_data: ParsedData = parse_sdl_file(args.input_file)

    # Generate output filename from input filename
    base_name = f"keysight{os.path.splitext(os.path.basename(args.input_file))[0].lower()}"
    output_filename = f"{base_name}.py"
    # Use the correct test file naming convention: test_<category>_<driver>.py
    test_filename = f"test_funcgenerators_{base_name}.py"
    
    # Combine output directory with filename if specified
    if args.output_dir:
        # Create output directory if it doesn't exist
        os.makedirs(args.output_dir, exist_ok=True)
        output_path = os.path.join(args.output_dir, output_filename)
    else:
        output_path = output_filename

    # Get the absolute path to the instrumental/tests/drivers directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
    test_dir = os.path.join(project_root, 'instrumental', 'tests', 'drivers')
    os.makedirs(test_dir, exist_ok=True)
    test_path = os.path.join(test_dir, test_filename)
    
    print(f"Writing test file to: {test_path}")
    
    # Generate all content
    content = []
    content.extend(generate_enums_file(parsed_data))
    content.extend(generate_command_syntaxes_file(parsed_data))
    content.append(generate_main_class(parsed_data, supported_models, args.input_file))  # Pass the SDL filename

    # Write everything to a single file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

    # Generate and write test file
    test_content = generate_test_file(parsed_data, supported_models, args.input_file)  # Pass the SDL filename
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(test_content)

    print(f"\nAll code has been written to {output_path}")
    print(f"Test file has been written to {test_path}")

    generate_info_file()

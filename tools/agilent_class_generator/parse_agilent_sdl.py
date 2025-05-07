from bs4 import BeautifulSoup, Tag, NavigableString
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Union, Any
from enum import Enum
from dataclasses import dataclass, field
from utils import sanitize_enum_name, get_python_type, get_python_type_converter


@dataclass(frozen=True)
class CustomSuffix:
    custom_suffix: str
    element_type: str

@dataclass(frozen=True)
class DecimalNumeric:
    custom_suffix: str
    element_type: str

@dataclass(frozen=True)
class ArbitraryBlock:
    element_format: str
    element_type: str

@dataclass(frozen=True)
class DefiniteLengthArbitraryBlock:
    element_format: str
    element_type: str
    separator: str

    def from_device(response: str):
        return np.array(response.split(self.separator))


@dataclass(frozen=True)
class EnumMember:
    mnemonic: str
    # aliases: str
    value: str
    description: Optional[str] = None

    def __eq__(self, other):
        if not isinstance(other, EnumMember):
            return False
        return self.mnemonic == other.mnemonic and self.value == other.value and self.description == other.description
    
    def __hash__(self):
        return hash((self.mnemonic, self.value, self.description))

@dataclass(frozen=True)
class GlobalDefinition:
    name: str
    members: List[EnumMember]

    def __eq__(self, other):
        if not isinstance(other, GlobalDefinition):
            return False
        if len(self.members) != len(other.members):
            return False
        # Compare the names of the members
        for member in self.members:
            if not any(member == other_member for other_member in other.members):
                return False

        # Check if the names are the same
        return self.name == other.name

    def __hash__(self):
        return hash((self.name, tuple(self.members)))

@dataclass(frozen=True)
class ParameterType:
    type_name: str
    enum_ref: Optional[str] = None

    def to_python_type(self: str) -> str:
        """
        Convert SCPI parameter type to Python type annotation.
            
        Returns:
            str: The corresponding Python type annotation
        """
        if self.enum_ref:
            return sanitize_enum_name(self.enum_ref)

        # Then check parameter type
        type_mapping = {
            "DecimalNumeric": "float",
            "NonDecimalNumeric": "int",
            "Character": "str",
            "String": "str",
            "Boolean": "bool",
            "Block": "bytes",
            "NR1Numeric": "int",
            "NR2Numeric": "float",
            "NR3Numeric": "float",
            "ArbitraryBlock": "bytes",
        }
        
        return type_mapping.get(self.type_name, "Any")

@dataclass(frozen=True)
class ResponseType:
    type_name: str
    enum_ref: Optional[str] = None

    def to_python_type(self) -> str:
        if self.enum_ref:
            return sanitize_enum_name(self.enum_ref)
        return self.type_name
    

@dataclass(frozen=True)
class ParameterData:
    name: str
    semantic_type: str
    description: str
    parameter_types: List[ParameterType]
    repeat: Optional[str] = None


    def to_python_type(self) -> str:
        """
        Convert SCPI parameter type to Python type annotation.
        
        Args:
            param_type: The SCPI parameter type (e.g., 'DecimalNumeric', 'String', etc.)
            semantic_type: The semantic type from the parameter (e.g., 'Boolean', 'Integer', etc.)
            
        Returns:
            str: The corresponding Python type annotation
        """
        # First check semantic type as it's more specific
        if self.semantic_type:
            semantic_mapping = {
                "Boolean": "bool",
                "Integer": "int",
                "Real": "float",
                "String": "str",
            }
            if self.semantic_type in semantic_mapping:
                return semantic_mapping[self.semantic_type]
        
        types = [param_type.to_python_type() for param_type in self.parameter_types]
        return f"Union[{', '.join(types)}] | None"

@dataclass(frozen=True)
class CommandSyntax:
    name: str
    parameters: List[ParameterData]

@dataclass(frozen=True)
class ResponseData:
    name: str
    semantic_type: str
    description: str
    response_types: List[ParameterType]

    def to_python_type(self) -> str:
        """
        Convert SCPI parameter type to Python type annotation.
        
        Args:
            param_type: The SCPI parameter type (e.g., 'DecimalNumeric', 'String', etc.)
            semantic_type: The semantic type from the parameter (e.g., 'Boolean', 'Integer', etc.)
            
        Returns:
            str: The corresponding Python type annotation
        """
        return get_python_type(self.semantic_type)

    def to_python_type_converter(self) -> str:
        """
        Convert SCPI parameter type to Python type annotation.
        
        Args:
            param_type: The SCPI parameter type (e.g., 'DecimalNumeric', 'String', etc.)
            semantic_type: The semantic type from the parameter (e.g., 'Boolean', 'Integer', etc.)
            
        Returns:
            str: The corresponding Python type annotation
        """
        return get_python_type_converter(self.semantic_type)

@dataclass(frozen=True)
class CommandInfo:
    synopsis: str
    has_query: bool
    has_write: bool
    path: List[str]
    command_syntaxes: List[CommandSyntax]
    responses: List[ResponseData]

@dataclass(frozen=True)
class NodeSuffix:
    name: str
    description: str
    min_value: Optional[int] = None
    max_value: Optional[int] = None

@dataclass(frozen=True)
class Node:
    mnemonic: str
    aliases: str
    suffixes: Optional[NodeSuffix] = None
    commands: List[CommandInfo] = field(default_factory=list)
    nodes: List['Node'] = field(default_factory=list)

@dataclass(frozen=True)
class ParsedData:
    global_definitions: Dict[str, GlobalDefinition]
    commands: List[CommandInfo]
    subsystems: List[Node]

class CommandType(Enum):
    QUERY = "Query"
    WRITE = "Write"
    BOTH = "Both"

def parse_response_type(response_type_node: Tag) -> List[ResponseType]:
    """
    Parse the ResponseType node and extract all possible types.
    
    Args:
        response_type_node: The ResponseType node from BeautifulSoup
        
    Returns:
        List[ParameterType]: List of response types with their details
    """
    types: List[ResponseType] = []
    
    # Get all direct children of ParameterType
    for type_node in response_type_node.children:
        if not isinstance(type_node, Tag):  # Skip text nodes
            continue
            
        # Check if this type has an EnumRef
        enum_ref = type_node.find('EnumRef')
        enum_name: Optional[str] = enum_ref.get('name', '') if enum_ref else None
        
        # Create ParameterType with the type name and enum reference
        types.append(ResponseType(type_node.name, enum_name))
    
    return types

def parse_parameter_type(param_type_node: Tag) -> List[ParameterType]:
    """
    Parse the ParameterType node and extract all possible types.
    Each type can have its own EnumRef nested within it.
    
    Args:
        param_type_node: The ParameterType node from BeautifulSoup
        
    Returns:
        List[ParameterType]: List of parameter types with their details
    """
    types: List[ParameterType] = []
    
    # Get all direct children of ParameterType
    for type_node in param_type_node.children:
        if not isinstance(type_node, Tag):  # Skip text nodes
            continue
            
        # Check if this type has an EnumRef
        enum_ref = type_node.find('EnumRef')
        enum_name: Optional[str] = enum_ref.get('name', '') if enum_ref else None
        
        # Create ParameterType with the type name and enum reference
        types.append(ParameterType(type_node.name, enum_name))
    
    return types

def parse_global_definitions(soup: BeautifulSoup) -> Dict[str, GlobalDefinition]:
    """
    Parse the GlobalDefinitions section and extract all enum information.
    
    Args:
        soup: BeautifulSoup object of the XML file
        
    Returns:
        Dict[str, GlobalDefinitions]: Dictionary containing all enum definitions
    """
    global_defs: Dict[str, GlobalDefinition] = {}
    
    # Find the GlobalDefinitions section
    global_defs_node = soup.find('GlobalDefinitions')
    if not global_defs_node:
        return global_defs
    
    # Parse all Enums in GlobalDefinitions
    for enum in global_defs_node.find_all('Enum'):
        enum_ref_name = enum.get('name', '')
        if not enum_ref_name:
            continue
        
        enum_name = enum.get('langTypeName', '')
        if not enum_name:
            enum_name = enum_ref_name
        
        for suffix in ['_command_parameter_1', '_query_response_1']:
            enum_name = enum_name.replace(suffix, "")

        members: List[EnumMember] = []
        # Parse all members of the enum
        for member in enum.find_all('Member'):
            member_data = EnumMember(
                mnemonic=member.get('mnemonic', ''),
                # aliases=member.get('aliases', ''),
                value=member.get('value', ''),
                description=member.find('Description').text if member.find('Description') else None
            )
            members.append(member_data)
        
        if enum_name in global_defs:
            existing_members = global_defs[enum_name].members
            if set(existing_members) != set(members):
                print(f"Warning: Duplicate enum name '{enum_name}' with different members found.")
                print(f"Existing members: {existing_members}")
                print(f"New members: {members}")
            continue
        global_defs[enum_ref_name] = GlobalDefinition(name=enum_name, members=members)
    
    return global_defs

def print_global_definitions(global_defs: Dict[str, GlobalDefinition]) -> None:
    """
    Print the global definitions in a readable format.
    
    Args:
        global_defs (Dict[str, GlobalDefinitions]): Dictionary containing global definitions
    """
    print("\n=== Global Definitions ===")
    for enum_name, enum_data in global_defs.items():
        print(f"\nEnum: {enum_data.name}")
        for member in enum_data.members:
            print(f"  - {member.mnemonic}")
            # if member.aliases:
                # print(f"    Aliases: {member.aliases}")
            if member.value:
                print(f"    Value: {member.value}")
            if member.description:
                print(f"    Description: {member.description}")

def get_command_path(node: Tag) -> List[str]:
    """
    Get the complete path of mnemonics from root to the current node.
    
    Args:
        node: The current node
        
    Returns:
        List[str]: List of mnemonics in the path
    """
    path: List[str] = []
    current: Optional[Tag] = node
    
    while current and current.name not in ['SubsystemCommands', 'CommonCommands']:
        # if current.name == 'Node':
        mnemonic = current.get('mnemonic', '')
        if mnemonic:
            path.insert(0, mnemonic)
        current = current.parent

    return [m for m in path if m]  # Remove empty strings

def get_command_syntax(path: List[str], has_query: bool, has_write: bool) -> str:
    """
    Generate the SCPI command syntax for a given command.
    
    Args:
        path (List[str]): List of mnemonics in the command path
        has_query (bool): Whether the command supports queries
        has_write (bool): Whether the command supports writes
        
    Returns:
        str: The complete SCPI command syntax
    """
    base_syntax = ':'.join(path)
    if has_query and has_write:
        return f"{base_syntax} [or {base_syntax}?]"
    elif has_query:
        return f"{base_syntax}?"
    else:  # has_write
        return base_syntax

def parse_command_node(command_node: Tag) -> CommandInfo:
    """
    Parse the Command node and extract all information about the command.
    """
    # Determine command type
    has_query: bool = bool(command_node.find('QuerySyntaxes'))
    has_write: bool = bool(command_node.find('CommandSyntaxes'))
    
    # Get the complete command path
    command_path: List[str] = get_command_path(command_node)
    
    # Parse command syntaxes
    command_syntaxes: List[CommandSyntax] = []
    if has_write:
        for cmd_syntax in command_node.find_all('CommandSyntax'):
            parameters: List[ParameterData] = []
            for param in cmd_syntax.find_all('Parameter'):
                param_type_node = param.find('ParameterType')
                semantic_type = param.get('semanticType', '')
                param_types = parse_parameter_type(param_type_node)
                
                param_data = ParameterData(
                    name=param.get('name', ''),
                    semantic_type=semantic_type,
                    description=param.get('description', ''),
                    parameter_types=param_types,
                    repeat=param.get('repeat') if param.get('repeat') else None
                )
                parameters.append(param_data)
            
            syntax_data = CommandSyntax(
                name=cmd_syntax.get('name', ''),
                parameters=parameters
            )
            command_syntaxes.append(syntax_data)
    
    # Parse responses from QuerySyntax
    responses: List[ResponseData] = []
    if has_query:
        for query_syntax in command_node.find_all('QuerySyntax'):
            for response in query_syntax.find_all('Response'):
                response_type_node = response.find('ResponseType')
                response_types = parse_response_type(response_type_node) if response_type_node else []
                
                response_data = ResponseData(
                    name=response.get('name', ''),
                    semantic_type=response.get('semanticType', ''),
                    description=response.get('description', ''),
                    response_types=response_types
                )
                responses.append(response_data)
    
    return CommandInfo(
        synopsis=command_node.find('Synopsis').text if command_node.find('Synopsis') else '',
        has_query=has_query,
        has_write=has_write,
        path=command_path,
        command_syntaxes=command_syntaxes,
        responses=responses
    )

def parse_node_suffixes(node: Tag) -> Optional[NodeSuffix]:
    """
    Parse the NodeSuffixes node and extract information about node suffixes.
    
    Args:
        node: The NodeSuffixes node from BeautifulSoup
        
    Returns:
        Optional[NodeSuffix]: Node suffix information if present, None otherwise
    """
    if not node:
        return None
        
    name = node.get('name', '')
    description = node.get('description', '')
    
    # Parse range if present
    range_node = node.find('NodeSuffixRange')
    min_value = None
    max_value = None
    if range_node:
        min_value = int(range_node.get('min', 0))
        max_value = int(range_node.get('max', 0))
    
    return NodeSuffix(name, description, min_value, max_value)

def parse_node(node: Tag) -> Node:
    """
    Parse a Node element and its children.
    
    Args:
        node: The Node element from BeautifulSoup
        
    Returns:
        Node: Parsed node information
    """
    mnemonic = node.get('mnemonic', '')
    aliases = node.get('aliases', '')
    
    # Parse node suffixes if present
    suffixes = parse_node_suffixes(node.find('NodeSuffixes', recursive=False))
    
    # Parse commands
    commands: List[CommandInfo] = []
    for cmd in node.find_all('SubsystemCommand', recursive=False):
        commands.append(parse_command_node(cmd))
    
    # Parse child nodes
    nodes: List[Node] = []
    for child in node.find_all('Node', recursive=False):
        nodes.append(parse_node(child))
    
    return Node(mnemonic, aliases, suffixes, commands, nodes)

def parse_sdl_file(file_path: str) -> ParsedData:
    """
    Parse the SDL file and extract useful information about SCPI commands.
    
    Args:
        file_path (str): Path to the SDL file
        
    Returns:
        ParsedData: Dataclass containing parsed information
    """
    # Read the XML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = str(file.read())
    
    # Parse with BeautifulSoup
    soup: BeautifulSoup = BeautifulSoup(content, 'xml')
    
    # Parse global definitions first
    global_defs: Dict[str, GlobalDefinition] = parse_global_definitions(soup)
    
    # Initialize result dictionary with proper typing
    result = ParsedData(
        global_definitions=global_defs,
        commands=[],
        subsystems=[]
    )
    
    # Parse CommonCommands section
    common_commands = soup.find('CommonCommands')
    if common_commands:
        for cmd in common_commands.find_all('CommonCommand'):
            result.commands.append(parse_command_node(cmd))
    
    # Parse commands and subsystems
    for root_node in soup.find_all('RootNode'):
        # Parse node suffixes if present
        suffixes = parse_node_suffixes(root_node.find('NodeSuffixes'))
        
        # Parse commands directly under root
        commands: List[CommandInfo] = []
        for cmd in root_node.find_all('SubsystemCommand', recursive=False):
            commands.append(parse_command_node(cmd))
        
        # Parse child nodes
        nodes: List[Node] = []
        for child in root_node.find_all('Node', recursive=False):
            nodes.append(parse_node(child))
        
        subsystem_data = Node(
            mnemonic=root_node.get('mnemonic', ''),
            aliases=root_node.get('aliases', ''),
            suffixes=suffixes,
            nodes=nodes,
            commands=commands
        )
        result.subsystems.append(subsystem_data)

    return result

def print_parsed_info(data: ParsedData) -> None:
    """
    Print the parsed information in a readable format.
    
    Args:
        data (ParsedData): Dataclass containing parsed information
    """
    # Print global definitions first
    print_global_definitions(data.global_definitions)
    
    print("\n=== Enums ===")
    for enum in data.enums:
        print(f"\nEnum: {enum.name}")
        for member in enum.members:
            print(f"  - {member.mnemonic} ({member.aliases}): {member.value}")
    
    print("\n=== Subsystems ===")
    for subsystem in data.subsystems:
        print(f"\nSubsystem: {subsystem.mnemonic} ({subsystem.aliases})")
        for subcommand in subsystem.subcommands:
            print(f"  Subcommand: {subcommand.mnemonic} ({subcommand.aliases})")
            for cmd in subcommand.commands:
                syntax = get_command_syntax(cmd.path, cmd.has_query, cmd.has_write)
                print(f"    Command: {cmd.synopsis}")
                print(f"    Type: {'Both' if cmd.has_query and cmd.has_write else 'Query' if cmd.has_query else 'Write'}")
                print(f"    Syntax: {syntax}")
                
                if cmd.command_syntaxes:
                    print("    Command Syntaxes:")
                    for syntax in cmd.command_syntaxes:
                        print(f"      Syntax: {syntax.name}")
                        if syntax.parameters:
                            print("      Parameters:")
                            for param in syntax.parameters:
                                print(f"        - {param.name} ({param.semantic_type})")
                                print(f"          Description: {param.description}")
                                print(f"          Parameter Types: {', '.join(str(pt) for pt in param.parameter_types)}")
                                if param.repeat:
                                    print(f"          Repeat: {param.repeat}")
                
                if cmd.responses:
                    print("    Responses:")
                    for response in cmd.responses:
                        print(f"      - {response.name} ({response.semantic_type})")
                        print(f"        Description: {response.description}")
                        print(f"        Response Types: {', '.join(str(rt) for rt in response.response_types)}")

def print_subsystem_commands(data: ParsedData, subsystem_name: str) -> None:
    """
    Print all commands for a specific subsystem.
    
    Args:
        data (ParsedData): Dataclass containing parsed information
        subsystem_name (str): Name of the subsystem to print commands for
    """
    subsystem_name = subsystem_name.upper()
    found: bool = False
    
    for subsystem in data.subsystems:
        print(f"{subsystem.mnemonic.upper()} == {subsystem_name} = {subsystem.mnemonic.upper() == subsystem_name}")
        if subsystem.mnemonic.upper() == subsystem_name:
            found = True
            print(f"\n=== Commands for {subsystem.mnemonic} ({subsystem.aliases}) ===")
            for cmd in subsystem.commands:
                syntax = get_command_syntax(cmd.path, cmd.has_query, cmd.has_write)
                print(f"  Command: {cmd.synopsis}")
                print(f"  Type: {'Both' if cmd.has_query and cmd.has_write else 'Query' if cmd.has_query else 'Write'}")
                print(f"  Syntax: {syntax}")
                
                if cmd.command_syntaxes:
                    print("  Command Syntaxes:")
                    for syntax in cmd.command_syntaxes:
                        print(f"    Syntax: {syntax.name}")
                        if syntax.parameters:
                            print("    Parameters:")
                            for param in syntax.parameters:
                                print(f"      - {param.name} ({param.semantic_type})")
                                print(f"        Description: {param.description}")
                                print(f"        Parameter Types: {', '.join(str(pt) for pt in param.parameter_types)}")
                                if param.repeat:
                                    print(f"        Repeat: {param.repeat}")
                
                if cmd.responses:
                    print("  Responses:")
                    for response in cmd.responses:
                        print(f"    - {response.name} ({response.semantic_type})")
                        print(f"      Description: {response.description}")
                        print(f"      Response Types: {', '.join(str(rt) for rt in response.response_types)}")

    if not found:
        print(f"\nNo subsystem found with name '{subsystem_name}'")
        print("\nAvailable subsystems:")
        for subsystem in data.subsystems:
            print(f"- {subsystem.mnemonic} ({subsystem.aliases})")

def extract_supported_models(idf_file: str) -> List[str]:
    """
    Extract the list of supported models from the IDF file.
    
    Args:
        idf_file (str): Path to the IDF file
        
    Returns:
        List[str]: List of supported model numbers
    """
    try:
        # Parse the XML file
        tree = ET.parse(idf_file)
        root = tree.getroot()
        
        # Define the namespace
        ns = {'scd': 'http://www.Agilent.com/schemas/SCD/2008'}
        
        # Check if root is ScpiConfigurations
        if root.tag.endswith('ScpiConfigurations'):
            models_str = root.get('supportedModels', '')
            # Split the comma-separated list and strip whitespace
            models = [model.strip() for model in models_str.split(',')]
            return models
            
        # If not root, try to find it
        scpi_config = root.find('.//scd:ScpiConfigurations', namespaces=ns)
        if scpi_config is not None:
            models_str = scpi_config.get('supportedModels', '')
            # Split the comma-separated list and strip whitespace
            models = [model.strip() for model in models_str.split(',')]
            return models
        else:
            print(f"Warning: Could not find ScpiConfigurations element in {idf_file}")
            return []
            
    except ET.ParseError as e:
        print(f"Error parsing IDF file: {e}")
        return []
    except Exception as e:
        print(f"Error reading IDF file: {e}")
        return []

if __name__ == "__main__":
    file_path: str = "33500B_program_reference/33500B.sdl"
    parsed_data: ParsedData = parse_sdl_file(file_path)
    
    # Print global definitions
    # print_global_definitions(parsed_data.global_definitions)
    
    # Example usage of the subsystem commands function
    # print_subsystem_commands(parsed_data, "DISPlay")
import re

def sanitize_enum_name(name: str) -> str:
    """
    Convert an enum name to a valid Python class name.

    Args:
        name (str): The original enum name

    Returns:
        str: A valid Python class name
    """
    # Remove any non-alphanumeric characters and convert to PascalCase
    name = re.sub(r"[^a-zA-Z0-9]", "_", name)
    words = name.split("_")
    
    return "".join(word.capitalize() for word in words if word)

def get_python_type(semantic_type: str) -> str:
    """
    Convert SCPI semantic type to Python type annotation.

    Args:
        semantic_type (str): The SCPI semantic type

    Returns:
        str: The corresponding Python type annotation
    """
    type_mapping = {
        "Boolean": "bool",
        "Integer": "int",
        "Real": "float",
        "String": "str",
        "1-D Array": "NDArray[Any]",
    }
    return type_mapping.get(semantic_type, "Any")

def get_python_type_converter(semantic_type: str) -> str:
    """
    Convert SCPI semantic type to Python type annotation.

    Args:
        semantic_type (str): The SCPI semantic type

    Returns:
        str: The corresponding Python type annotation
    """
    type_mapping = {
        "Boolean": "bool",
        "Integer": "int",
        "Real": "float",
        "String": "str",
        "1-D Array": "np.array",
        "DefiniteLengthArbitraryBlock": "np.array()",
    }
    return type_mapping.get(semantic_type, "Any")


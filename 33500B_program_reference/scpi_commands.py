"""
SCPI Commands for Keysight 33500B Series Waveform Generator
This file contains structured information about all available SCPI commands.
"""

from dataclasses import dataclass
from typing import List, Optional, Union

@dataclass
class CommandParameter:
    name: str
    type: str
    description: str
    optional: bool = False
    default: Optional[str] = None

@dataclass
class Command:
    name: str
    subsystem: str
    description: str
    read_only: bool
    parameters: List[CommandParameter]
    return_type: Optional[str]
    return_description: Optional[str]
    example: Optional[str] = None

# Dictionary to store all commands
commands: dict[str, Command] = {}

# Example of how a command will be structured:
# commands["VOLT"] = Command(
#     name="VOLT",
#     subsystem="VOLTage",
#     description="Sets the output voltage level",
#     read_only=False,
#     parameters=[
#         CommandParameter(
#             name="amplitude",
#             type="float",
#             description="Voltage amplitude in volts"
#         )
#     ],
#     return_type=None,
#     return_description=None
# )

# The actual commands will be added here as we parse the documentation 
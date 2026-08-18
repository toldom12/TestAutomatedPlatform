from dataclasses import dataclass
from enum import StrEnum, Enum


class ArduinoCommand(StrEnum):
    STATUS = "STATUS"
    TEMP = "TEMP"
    NONE = "NONE"
    SELFTEST = "SELFTEST"

class ArduinoExpectedStatus(StrEnum):
    OK = "OK"
    TEMP = "24.5"

@dataclass
class CreateCaseArduino:
    send_cmd: ArduinoCommand
    received_cmd: str


class CasePingArduino(Enum):
    case_STATUS = CreateCaseArduino(send_cmd=ArduinoCommand.STATUS, received_cmd=ArduinoExpectedStatus.OK)
    case_TEMP = CreateCaseArduino(send_cmd=ArduinoCommand.TEMP, received_cmd=ArduinoExpectedStatus.TEMP)
    case_NONE = CreateCaseArduino(send_cmd=ArduinoCommand.NONE, received_cmd=ArduinoExpectedStatus.OK)

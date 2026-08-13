from dataclasses import dataclass
from enum import StrEnum, Enum
from typing import Optional


@dataclass
class EncoderInfo:
    com_port : str
    boundrate: int
    stepper_motor_steps :int
    case: Optional[StrEnum] = None



class CheckCommunicationEnocderCase(Enum):
    case_0 = EncoderInfo(com_port='COM3',
                         boundrate=115200,
                         stepper_motor_steps=200)


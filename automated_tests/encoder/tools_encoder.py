from dataclasses import dataclass
from enum import StrEnum, Enum, IntEnum
from typing import Optional

from automated_tests.encoder.map import StartUp
from tools.StepsVerifcator.steps_verifcator import TesStepsVerifcator
from tools.encoder.tools_encoder_handling import EncoderHandling, Commands


@dataclass
class EncoderInfo:
    com_port : str = 'COM9'
    boundrate: int = 999999
    stepper_motor_steps :int = 9999
    case: Optional[StrEnum] = None
    valve_steps : int = 1000
    cmd_encoder : Commands = Commands.ReadPosition

class CaseEnocderRotateCheck(StrEnum):
    NoRotate = 'NoRotate'
    Rotate = 'Rotate'

class CheckCommunicationEnocderCase(Enum):
    case_0 = EncoderInfo(com_port='COM3',
                         boundrate=115200,
                         stepper_motor_steps=200)

class CheckRotateMeasurementEncoder(Enum):
    case_0 = EncoderInfo(case = CaseEnocderRotateCheck.NoRotate,
                         valve_steps= 999,
                         cmd_encoder=Commands.ReadPosition)

class EncoderPlatform:
    @staticmethod
    def check_encoder_connection(encoder_init_params: EncoderHandling,
                           expected_parameters_encoder :EncoderInfo,
                           test: TesStepsVerifcator) -> TesStepsVerifcator:

        test.add_test(condition=bool(encoder_init_params.port == expected_parameters_encoder.com_port),
                      fail_msg=f'[ID_0] Not correctly port COM, '
                               f'encoder_received: {encoder_init_params.port},'
                               f'encoder_expected: {expected_parameters_encoder.com_port},'
                               f'')

        test.add_test(condition=bool(encoder_init_params.boundrate == expected_parameters_encoder.boundrate),
                      fail_msg=f'[ID_1] Not correctly boundrate , '
                               f'encoder_received: {encoder_init_params.boundrate},'
                               f'encoder_expected: {expected_parameters_encoder.boundrate},'
                               f'')

        test.add_test(condition=bool(encoder_init_params.stepper_steps_per_rotation ==
                                     expected_parameters_encoder.stepper_motor_steps),
                      fail_msg=f'Not stepper motor steppes '
                               f'encoder_received: {encoder_init_params.stepper_steps_per_rotation},'
                               f'encoder_expected: {expected_parameters_encoder.stepper_motor_steps},'
                               f'')

        return test
    @staticmethod
    def get_case_name(expected_data_encoder : EncoderInfo) -> StrEnum:
        get_case_name = expected_data_encoder.case
        return get_case_name

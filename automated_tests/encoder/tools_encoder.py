from dataclasses import dataclass
from enum import StrEnum, Enum
from typing import Optional

from automated_tests.encoder.map import StartUp
from tools.StepsVerifcator.steps_verifcator import TesStepsVerifcator
from tools.encoder.tools_encoder_handling import EncoderHandling


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

import pytest

from automated_tests.arduino.map import StartUp
from automated_tests.arduino.tools_arduino import ArduinoCommand, CasePingArduino, CreateCaseArduino
from tools.StepsVerifcator.steps_verifcator import TesStepsVerifcator

@pytest.mark.parametrize("data_params", [params.value for params in CasePingArduino])
def test_ping_arduino(module_data:StartUp,
                      data_params:CreateCaseArduino):

    test = TesStepsVerifcator()

    module_data.arduino_nano.send_frame(command=data_params.send_cmd)

    response = module_data.arduino_nano.receive_frame(sended_command=data_params.send_cmd)

    test.add_test(condition=bool(response == data_params.received_cmd),
                  fail_msg=f'[ID_0][FAIL] mis match params:{response},'
                           f'{data_params.send_cmd} ')

    assert test.expected_results == test.received_results

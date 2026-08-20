import pytest

from automated_tests.encoder.map import StartUp
from automated_tests.encoder.tools_encoder import CheckCommunicationEnocderCase, EncoderInfo, EncoderPlatform, \
    CheckRotateMeasurementEncoder, CaseEnocderRotateCheck
from tools.StepsVerifcator.steps_verifcator import TesStepsVerifcator


@pytest.mark.parametrize('parameters_encoder', [
       params.value for params in CheckCommunicationEnocderCase])
def test_check_startup_params_encoder(module_data: StartUp,
                                     parameters_encoder : EncoderInfo):
      '''
      Test case (ID : 12345): Check encoder startup parameters .

      Steps:
      1. Create the encoder handler using the settings from setup/config.ini.
      2. Load the expected encoder parameters from the test case data.
      3. Verify that the configured COM port matches the expected COM port.
      4. Verify that the configured baud rate matches the expected baud rate.
      5. Verify that the configured number of stepper-motor steps per rotation
         matches the expected value.

      Expected result:
      All configured encoder parameters match the expected test-case values.
      '''

      test = TesStepsVerifcator()

      EncoderPlatform.check_encoder_connection(encoder_init_params=module_data.encoder,
                                               expected_parameters_encoder=parameters_encoder,
                                               test = test)

      assert test.received_results == test.expected_results

@pytest.mark.parametrize('parameters_encoder', [
       params.value for params in CheckRotateMeasurementEncoder])
def test_check_rotate_value_from_encoder(module_data: StartUp,
                                         parameters_encoder : EncoderInfo):
    """
    Test case (ID : 54321): Check encoder position when the motor does not rotate.

    Steps:
    1. Read the test-case type and confirm that it is NoRotate.
    2. Send the ReadPosition command to the encoder and calculate the valve
       position as a percentage using the configured valve travel.
    3. Do not command the stepper motor to move.
    4. Send the ReadPosition command to the encoder a second time and calculate
       the position percentage again.
    5. Compare the first and second calculated position values.

    Expected result:
    Both measurements are equal because the stepper motor has not moved.
    """

    test = TesStepsVerifcator()

    case_name = EncoderPlatform.get_case_name(expected_data_encoder=parameters_encoder)

    if case_name  == CaseEnocderRotateCheck.NoRotate:
        get_first_measuremet = module_data.encoder.execute_measurement_in_percentage(
            valve_steps=parameters_encoder.valve_steps,
            cmd= parameters_encoder.cmd_encoder)

        # --> No rotate stepper motor

        get_second_measurement = module_data.encoder.execute_measurement_in_percentage(
            valve_steps=parameters_encoder.valve_steps,
            cmd= parameters_encoder.cmd_encoder)


        test.add_test(condition=bool(get_first_measuremet == get_second_measurement),
                      fail_msg=f'[ID_3] Not correctly measurement stepper paramrs:,'
                               f'1: {get_first_measuremet},'
                               f'2: {get_second_measurement}')

        assert test.received_results == test.expected_results

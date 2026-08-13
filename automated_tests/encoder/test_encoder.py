import pytest

from automated_tests.encoder.map import StartUp
from automated_tests.encoder.tools_encoder import CheckCommunicationEnocderCase, EncoderInfo, EncoderPlatform
from tools.StepsVerifcator.steps_verifcator import TesStepsVerifcator


@pytest.mark.parametrize('parameters_encoder', [
       params.value for params in CheckCommunicationEnocderCase])
def test_check_communication_encoder(module_data: StartUp,
                                     parameters_encoder : EncoderInfo):


      test = TesStepsVerifcator()

      EncoderPlatform.check_encoder_connection(encoder_init_params=module_data.encoder,
                                               expected_parameters_encoder=parameters_encoder,
                                               test = test)



      assert test.received_results == test.expected_results






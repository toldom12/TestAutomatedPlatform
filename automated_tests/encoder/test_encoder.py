import pytest

from automated_tests.encoder.map import StartUp
from automated_tests.encoder.tools_encoder import CheckCommunicationEnocderCase, EncoderInfo


@pytest.mark.parametrize('data_parameters', [
       params.value for params in CheckCommunicationEnocderCase])
def test_check_communication_encoder(module_data: StartUp,
                                     data_parameters : EncoderInfo):

      info = module_data.encoder
      pass





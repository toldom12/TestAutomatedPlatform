import pytest
import serial

from automated_tests.encoder.map import StartUp
from setup.configurator import com_port, boundrate
from tools.encoder.tools_encoder_handling import EncoderHandling


@pytest.fixture(autouse = True, scope = 'module')
def module_data():
    init : StartUp = StartUp(encoder = EncoderHandling(port=com_port,
                            parity=serial.PARITY_NONE,
                            boundrate=boundrate))

    yield init

    return 0


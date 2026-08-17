from typing import Any, Generator

import pytest

from automated_tests.arduino.map import StartUp
from tools.arduino.arduino import Arduino

is_flash_is_needed : bool = False

@pytest.mark(autouse = True, scope = 'module')
def module_data() -> Generator[StartUp, Any, None]:
    arduino = Arduino()
    init: StartUp = StartUp(arduino_nano = arduino)

    if is_flash_is_needed:
        init.arduino_nano.erase_device()
        init.arduino_nano.flash_device(wait_after=5)

    yield init

    return None


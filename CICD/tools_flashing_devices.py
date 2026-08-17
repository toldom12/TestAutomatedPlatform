from dataclasses import dataclass
from enum import StrEnum


def extract_prefix(parameters: list[str]) -> list:
    clean_parameters: list[str] = []
    for params in parameters:
        p = params.removeprefix("--")
        clean_parameters.append(p)

    return clean_parameters


class TestType(StrEnum):
    Selftest = "selftest"
    SystemTest = "systemtest"
    IntegrationTest = "integration_test"
    WithoutTest = "no_test"

class FlashingDevice(StrEnum):
    ArduinoNano = "arduino_nano"
    JLink  = "jlink"

class FlashingType(StrEnum):
    Flash = "flash"
    Erase = "erase"

@dataclass
class FlashObjects:
    device_type : FlashingDevice
    flash_type : FlashingType
    test_type : TestType


import pytest

from CICD.tools_flashing_devices import (
    FlashObjects,
    FlashingDevice,
    extract_prefix,
    FlashingType,
    TestType,
)
from tools.arduino.arduino import Arduino



def get_test_configuration(request) -> FlashObjects:
    raw_arguments = request.config.getoption("--test_args")

    print(f"TEST ARGS: {raw_arguments}")

    parameters = extract_prefix(raw_arguments.split())

    if len(parameters) != 3:
        raise ValueError(
            "Expected 3 parameters; "
            f"received: {parameters}"
        )

    return FlashObjects(
        device_type=FlashingDevice(parameters[0]),
        flash_type=FlashingType(parameters[1]),
        test_type=TestType(parameters[2]),
    )


def test_run_selftest(request):
    configuration = get_test_configuration(request)

    if configuration.test_type == TestType.Selftest:
        ino = Arduino()
        ino.erase_device()
        ino.flash_device(wait_after=5)




if __name__ == "__main__":
    pass

        #--test_args="--arduino_nano --flash --selftest" -vv -s
       # python -m pytest CICD\selftest\test_perform_selftest.py::test_run_selftest --test_args="--arduino_nano --flash --selftest" -vv
        # pytest.main([
        #     r"C:\Repos\AutomatedTestsEmbeddedPlatform\CICD\selftest\test_perform_selftest.py::test_run_selftest",
        #     "--test_args=--arduino_nano --flash --selftest",
        #     "-vv",
        #     "-s",
        # ])
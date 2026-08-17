import argparse

from CICD.tools_flashing_devices import extract_prefix, FlashObjects, FlashingDevice, FlashingType
from tools.arduino.arduino import Arduino

parser = argparse.ArgumentParser()
_ , parameters = parser.parse_known_args()

if len(parameters) != 2:
    raise  parser.error(f"Expected two parameters, parmaters: {parameters}")


parameters = extract_prefix(parameters = parameters)

print(parameters)

create_flash_obj :FlashObjects = FlashObjects(device_type=parameters[0],
                                              flash_type= parameters[1],
                                              test_type=parameters[2]
                                              )

if create_flash_obj.device_type in FlashingDevice.ArduinoNano:
    A = Arduino()
    if create_flash_obj.flash_type in FlashingType.Flash:
        output_erase  = A.erase_device()
        output_flash = A.flash_device()
    if create_flash_obj.flash_type in FlashingType.Erase:
        output_flash = A.flash_device()


if __name__ == "__main__":
    pass
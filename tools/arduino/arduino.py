from enum import StrEnum

from setup import configurator
import subprocess


class ArduinoType(StrEnum):
    ArduinoNano = "arduino:avr:nano"

class Arduino:
    def __init__(self,
                 arduino_cli_path : str= configurator.arduino_cli,
                 com_port: int = configurator.arduino_nano_com_port,
                 name_board: StrEnum = ArduinoType.ArduinoNano,
                 boundrate : int = configurator.arduino_nano_boudrate,
                 ):
        self.name_board = name_board
        self.com_port = com_port
        self.boudrate = boundrate
        self.arduino_cli_path = arduino_cli_path


    def flash_device(self,
                     flash_path: str = configurator.arduino_nano_flash_path):
        if self.name_board == ArduinoType.ArduinoNano:
            try:
                output = subprocess.run([self.arduino_cli_path, "compile",
                                         "--fqbn", "arduino:avr:nano:cpu=atmega328old",
                                         "--upload",
                                         "--port", self.com_port,
                                         flash_path
                ],
                check=True,
                text=True,
                capture_output=True,
                encoding='utf-8')

                return output
            except Exception as f:
                print(f'[{ArduinoType.ArduinoNano}][ERROR]: {f}')
        return None

    def erase_device(self,
                     erase_path: str = configurator.arduino_nano_erase):
        if self.name_board == ArduinoType.ArduinoNano:
            try:
                output = subprocess.run([self.arduino_cli_path, "compile",
                                         "--fqbn", "arduino:avr:nano:cpu=atmega328old",
                                         "--upload",
                                         "--port", self.com_port,
                                         erase_path],
                                        check=True,
                                        text=True,
                                        capture_output=True,
                                        encoding='utf-8')
                return output
            except Exception as f:
                print(f'[{ArduinoType.ArduinoNano}][ERROR]: {f}')
        return None
if __name__ =='__main__':
    a = Arduino()
    c = a.erase_device()
    z = a.flash_device()
    pass
    pass





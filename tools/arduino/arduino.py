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
                 file_path: str = configurator.arduino_nano_load_file
                 ):
        self.name_board = name_board
        self.com_port = com_port
        self.boudrate = boundrate
        self.file_path = file_path
        self.arduino_cli_path = arduino_cli_path


    def flash_device(self):
        if self.name_board == ArduinoType.ArduinoNano:
            output = subprocess.run([self.arduino_cli_path, "compile",
                                     "--fqbn", "arduino:avr:nano:cpu=atmega328old",
                                     "--upload",
                                     "--port", self.com_port,
                                     self.file_path

            ],
            check=True,
            text=True,
            capture_output=True,
            encoding='utf-8')

            return output
        return None


if __name__ =='__main__':
    a = Arduino()
    z = a.flash_device()
    pass




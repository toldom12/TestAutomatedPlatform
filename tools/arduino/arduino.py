import time
from enum import StrEnum
from time import sleep

import serial

from automated_tests.arduino.tools_arduino import ArduinoCommand
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
                 arduino = None):
        self.name_board = name_board
        self.com_port = com_port
        self.boudrate = boundrate
        self.arduino_cli_path = arduino_cli_path
        self.arduino = arduino
        self.arduino = serial.Serial(port=str(self.com_port),
                                     baudrate=self.boudrate,
                                     timeout=3)
        self.arduino.close()
        self.arduino.open()
        time.sleep(3)

    def flash_device(self,
                     flash_path: str = configurator.arduino_nano_flash_path,
                     wait_before: float = 1,
                     wait_after: float = 1,
                     ):
        if self.name_board == ArduinoType.ArduinoNano:
            try:
                self.arduino.close()
                sleep(wait_before)
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

                sleep(wait_after)

                return output
            except Exception as f:
                print(f'[{ArduinoType.ArduinoNano}][ERROR]: {f}')
            finally:
                if not self.arduino.is_open:
                    self.arduino.open()
                time.sleep(wait_after)
        return None

    def erase_device(self,
                     erase_path: str = configurator.arduino_nano_erase,
                     wait_before: float = 1,
                     wait_after: float = 1,
                     ):
        if self.name_board == ArduinoType.ArduinoNano:
            try:
                self.arduino.close()
                sleep(wait_before)
                output = subprocess.run([self.arduino_cli_path, "compile",
                                         "--fqbn", "arduino:avr:nano:cpu=atmega328old",
                                         "--upload",
                                         "--port", self.com_port,
                                         erase_path],
                                        check=True,
                                        text=True,
                                        capture_output=True,
                                        encoding='utf-8')
                sleep(wait_after)
                return output
            except Exception as f:
                print(f'[{ArduinoType.ArduinoNano}][ERROR]: {f}')
            finally:
                if not self.arduino.is_open:
                    self.arduino.open()
                time.sleep(wait_after)
        return None

    def send_frame(self,
                     command: ArduinoCommand = ArduinoCommand.STATUS):

        time.sleep(3)
        # self.arduino.close()
        # self.arduino.open()
        self.arduino.reset_input_buffer()

        cmd = f'{command.value}\n'.encode("ascii")
        self.arduino.write(cmd)
        self.arduino.flush()


    def receive_frame(self,
                      sended_command: ArduinoCommand = ArduinoCommand.STATUS ):
        read_list : list[str] = []
        for i in range(len(sended_command)):
            read  = self.arduino.readline().decode("utf-8", errors = "replace").strip()
            if not read:
                break
            if read.isdigit():
                letter = chr(int(read))
                read_list.append(letter)
            else:
                read_list.append(read)

        txt = ''.join(read_list)
        return txt

    def close(self):
        self.arduino.close()

    def open(self):
        self.arduino.open()

if __name__ =='__main__':
    a = Arduino()
    c = a.erase_device()
    z = a.flash_device()
    a.send_frame()
    a.receive_frame()
    a.arduino.close()
    pass

    pass
    pass





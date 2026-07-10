import struct
import time
from enum import StrEnum, IntEnum

import serial
from setup.configurator import com_port, boundrate


class Commands(IntEnum):
    ReadPosition = 0x54
    ReadTurnsCounter = 0x55
    ExtendedCommands = 0x56

class ExtendedCommands(IntEnum):
    SetZeroPosition = 0x5E
    ResetEncoder = 0x75


class EncoderHandling:
    def __init__(self,
                 port: str  ,
                 boundrate: int,
                 parity: str):

        self.boundrate = boundrate
        self.port = port
        self.parity = parity

        self.serial = serial.Serial(port = self.port,
                                    baudrate=self.boundrate,
                                    parity=parity)

        self.serial.close()
        self.serial.open()
        self.serial.reset_input_buffer()

    def execute_command_encoder(self,
                                cmd: Commands) -> int:
        convert_data = bytes([cmd])
        self.serial.write(convert_data)

        response = self.serial.read(2)

        if len(response) != 2:
            raise f'Encoder loss bits {response} '

        raw = struct.unpack("<H", response)[0]

        position = raw & 0x3FFF # rmv first 2 bits to extract clean position for  encoder

        return position

    def execute_extended_commands(self,
                                  cmd: ExtendedCommands,
                                  wait_before : int | float = 0.1,
                                  wait_after: int | float = 0.1) -> None:

        extended_command= bytes([Commands.ExtendedCommands, cmd])

        time.sleep(wait_before)
        self.serial.write(extended_command)
        self.serial.flush()
        time.sleep(wait_after)













if __name__ == '__main__':
    e = EncoderHandling(port=com_port,
                        parity=serial.PARITY_NONE,
                        boundrate=boundrate)
    pos1 = e.execute_command_encoder(cmd = Commands.ReadTurnsCounter)

    pos2 = e.execute_command_encoder(cmd = Commands.ReadTurnsCounter)
    pass









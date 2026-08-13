import struct
import time
from enum import StrEnum, IntEnum

import serial

from setup.configurator import stepper_motor_steps, com_port, boundrate


class Commands(IntEnum):
    ReadPosition = 0x54
    ReadTurnsCounter = 0x55
    ExtendedCommands = 0x56

class ExtendedCommands(IntEnum):
    SetZeroPosition = 0x5E
    ResetEncoder = 0x75

class EncoderInfo(IntEnum):
    ENCODER_COUNTS_PER_ROTATION = 16_384 # 14 bits max value


class EncoderHandling:
    def __init__(self,
                 port: str  ,
                 boundrate: int,
                 parity: str,
                 stepper_steps_per_rotation: int = stepper_motor_steps,
                 encoder_counts_per_rotation: int = EncoderInfo.ENCODER_COUNTS_PER_ROTATION):

        self.boundrate = boundrate
        self.port = port
        self.parity = parity
        self.stepper_steps_per_rotation = stepper_steps_per_rotation
        self.encoder_counts_per_rotation = encoder_counts_per_rotation


        self.serial = serial.Serial(port = self.port,
                                    baudrate=self.boundrate,
                                    parity=parity)

        self.serial.close()
        self.serial.open()
        self.serial.reset_input_buffer()

    def initialize_encoder(self):
        encoder_counts_per_step = self.encoder_counts_per_rotation / self.stepper_steps_per_rotation
        return encoder_counts_per_step

    def execute_command_encoder(self,
                                cmd: Commands) -> int:
        convert_data = bytes([cmd])
        self.serial.write(convert_data)

        response = self.serial.read(2)

        if len(response) != 2:
            raise RuntimeError(f'Encoder loss bits {response}')

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

    def execute_measurement_in_percentage(self,
                                         valve_steps: int,
                                         cmd : Commands) -> float:
        if valve_steps <=0:
            raise ValueError(f' value should be greather than 0 ')
        stepper_per_rotation = self.initialize_encoder()
        position = self.execute_command_encoder(cmd= cmd)

        full_travel_encoder_counts = valve_steps * stepper_per_rotation

        calculate_percentage = (position / full_travel_encoder_counts)  * 1_0_0
        return calculate_percentage

    @property
    def get_row_position(self) -> int:
        position = self.execute_command_encoder(cmd= Commands.ReadPosition)
        return position




if __name__ == '__main__':
    e = EncoderHandling(port=com_port,
                        parity=serial.PARITY_NONE,
                        boundrate=boundrate)
    # pos1 = e.execute_command_encoder(cmd = Commands.ReadTurnsCounter)
    #
    # pos2 = e.execute_command_encoder(cmd = Commands.ReadTurnsCounter)
    pass

    pos1 = e.execute_measurement_in_percentage(cmd = Commands.ReadPosition,
                                               valve_steps=200)

    pos2 = e.execute_measurement_in_percentage(cmd = Commands.ReadPosition,
                                               valve_steps=200)

    pass










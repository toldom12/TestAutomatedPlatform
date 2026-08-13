
from setup.configurator import board_1, jlink_path
import subprocess

tmp = 'STM32F407VG'


class Jlink:
    def __init__(self,
                 serial_number: int = board_1,
                 jlink_path: str = jlink_path):

        self.serial_number = serial_number
        self.jlink_path = jlink_path

    def connect_jlink(self):
        output = subprocess.run([
            f"{self.jlink_path}",
            "-SelectEmuBySN", str(self.serial_number),
            "-Device", tmp,
            "-If", "SWD",
            "-Speed", "4000",
            "-AutoConnect", "1",
        ])



if __name__ == '__main__':
    a = Jlink()
    a.connect_jlink()
    pass


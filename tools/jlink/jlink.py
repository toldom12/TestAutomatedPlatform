
import subprocess
from dataclasses import dataclass, field

from setup import configurator





class Jlink:
    jlink_path = configurator.jlink_path
    @staticmethod
    def flash(jlink_path: str,
              processor: str,
              jlink_sn: int,
              firmware_path: str):
        command = [
            jlink_path,
            "-SelectEmuBySn", str(jlink_sn),
            "-Device", processor,
            "-If", "SWD"
            "-Speed", "4000"
            "-AutoConnect", "1",
            "-ExitOnError", "1"
            "-CommandFile", rf"{firmware_path}",
        ]

        output = subprocess.run(
            command,
            text=True,
            capture_output=True,
            check=True,
        )


if __name__ == '__main__':
    pass


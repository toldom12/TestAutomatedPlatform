
import subprocess
from pathlib import Path

from setup import configurator

DIR_PATH = Path(__file__).resolve().parent / 'tmp_files'

def build_command_jlink(parameters_list : list) -> str:
    path_to_jlink_file = f'{DIR_PATH}\\tmp.jlink'
    with open(rf'{path_to_jlink_file}', 'w') as f:
        for param in parameters_list:
            f.write(param + '\n')

    return path_to_jlink_file


#@TODO : add PID handling
#@TODO: reset  microporcessor
class Jlink:

    jlink_path = configurator.jlink_path
    
    @staticmethod
    def flash(jlink_path: str,
              processor: str,
              jlink_sn: int,
              hex_file: str):

        output = None
        jlink_command_file = build_command_jlink(parameters_list=[
            'connect'
            'erase',
             f'loadfile {hex_file}',
             'r',
             'q'])

        command = [
            jlink_path,
            "-SelectEmuBySn", str(jlink_sn),
            "-Device", processor,
            "-If", "SWD"
            "-Speed", "4000"
            "-AutoConnect", "1",
            "-ExitOnError", "1"
            "-CommandFile", rf"{jlink_command_file}",
        ]

        try:

            output = subprocess.run(
                command,
                text=True,
                capture_output=True,
                check=True,
            )
        except Exception as error:
            print(f'[ERROR][JFlash]: flash {error},'
                  f'ouptut: {output.stdout}')

    @staticmethod
    def erase(jlink_path: str,
              processor: str,
              jlink_sn: int):

        output = None
        jlink_command_file = build_command_jlink(parameters_list=[
            'connect',
            'erase',
            'exit'
        ])

        command = [
            jlink_path,
            "-SelectEmuBySn", str(jlink_sn),
            "-Device", processor,
            "-If", "SWD"
             "-Speed", "4000"
            "-AutoConnect", "1",
            "-ExitOnError", "1"
                            "-CommandFile", rf"{jlink_command_file}",
        ]

        try:
            output = subprocess.run(
                command,
                text=True,
                capture_output=True,
                check=True,
            )
        except Exception as error:
            print(f'[ERROR][JFlash] erase: {error},'
                  f'output: {output.stdout}')



if __name__ == '__main__':
    # load_file = 'C:\\Repos\\AutomatedTestsEmbeddedPlatform\\artifacts\\arduino\\nano\\flash\\flash.ino'
    # z = build_command_jlink(parameters_list=['erase',
    #                                      f'loadfile {load_file}',
    #                                      'r',
    #                                      'q'
    #                                          ])

    pass




import subprocess
from pathlib import Path

from setup import configurator

DIR_PATH = Path(__file__).resolve().parent / 'tmp_files'
RTT_LOGS_PATH = Path(__file__).resolve().parent / 'logs'/'rtt'


def build_command_jlink(parameters_list : list,
                        path_to_jlink_file: str = DIR_PATH / 'tmp.jlink')-> str:
    DIR_PATH.mkdir(parents=True, exist_ok=True)
    with open(path_to_jlink_file,'w') as f:
        for param in parameters_list:
            f.write(param + '\n')

    return str(path_to_jlink_file)


#@TODO : add PID handling
#@TODO: reset  microporcessor
class Jlink:

    jlink_path = configurator.jlink_path
    rtt_viewer_path = configurator.rtt_viewer_path

    @staticmethod
    def flash(
              processor: str,
              jlink_sn: int,
              hex_file: str):

        output = None
        jlink_command_file = build_command_jlink(parameters_list=[
            'connect',
            'erase',
             f'loadfile {hex_file}',
             'r',
             'q'])

        command = [
            Jlink.jlink_path,
            "-SelectEmuBySn", str(jlink_sn),
            "-Device", processor,
            "-If", "SWD",
            "-Speed", "4000",
            "-AutoConnect", "1",
            "-ExitOnError", "1",
            "-CommandFile", rf"{jlink_command_file}",
        ]

        try:

            output = subprocess.run(
                command,
                text=True,
                capture_output=True,
                check=True,
            )
        except subprocess.CalledProcessError as error:
            print(f'[ERROR][JFlash]: flash {error},'
                  f'output: {error.stdout}\n{error.stderr}')

    @staticmethod
    def erase(processor: str,
              jlink_sn: int):

        output = None
        jlink_command_file = build_command_jlink(parameters_list=[
            'connect',
            'h',
            'erase',
            'exit'
        ])

        command = [
            Jlink.jlink_path,
            "-SelectEmuBySn", str(jlink_sn),
            "-Device", processor,
            "-If", "SWD",
            "-Speed", "4000",
            "-AutoConnect", "1",
            "-ExitOnError", "1",
            "-CommandFile", rf"{jlink_command_file}",
        ]

        try:
            output = subprocess.run(
                command,
                text=True,
                capture_output=True,
                check=True,
            )
        except subprocess.CalledProcessError as error:
            print(f'[ERROR][JFlash] erase: {error},'
                  f'output: {error.stdout}\n{error.stderr}')


    @staticmethod
    def run_rtt_viewer(processor: str,
                       jlink_sn: int,
                       rtt_adress: int):
        RTT_LOGS_PATH.mkdir(parents=True, exist_ok=True)

        rtt_logs_path = RTT_LOGS_PATH / 'log.txt'

        jlink_command_file = build_command_jlink(parameters_list=[
            'connect',
            f'rtt start {rtt_adress}',
        ])

        process = subprocess.Popen([
            Jlink.jlink_path,
            '-SelectEmuBySn', str(jlink_sn),
            '-Device', processor,
            '-If', 'SWD',
            '-Speed', '4000',
            '-AutoConnect', '1',
            '-CommanderScript', jlink_command_file,
        ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)


        try:
            with rtt_logs_path.open('w', encoding='utf-8') as log:
                while process.poll() is None:
                    line = process.stdout.readline()
                    if line:
                        log.write(line)
                        print(line.strip())
        except KeyboardInterrupt:
            process.terminate()
            process.wait()





if __name__ == '__main__':
   # Jlink.erase(processor=configurator.board_1_uc,
   #             jlink_sn=configurator.board_1_sn)
   Jlink.run_rtt_viewer(processor=configurator.board_1_uc,
                        jlink_sn = configurator.board_1_sn,
                        rtt_adress=configurator.board_1_address)



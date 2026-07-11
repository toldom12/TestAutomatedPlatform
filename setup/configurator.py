import configparser
from pathlib import Path

config = configparser.ConfigParser()
config_path = Path(__file__).parent / "config.ini"
try:
    data = config.read(filenames = config_path)

    sections = config.sections()

    com_port = config.get(section='Encoder', option ='port_com')
    boundrate = config.getint(section='Encoder', option ='boundrate')
    stepper_motor_steps = config.getint(section='Encoder', option = 'stepper_motor_steps')


except  Exception as f:
    print(f'Is not possible open file {f}')












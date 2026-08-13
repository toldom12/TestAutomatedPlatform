import configparser
from pathlib import Path

config = configparser.ConfigParser()
config_path = Path(__file__).parent / "config.ini"
try:
    data = config.read(filenames = config_path)

    sections = config.sections()

    com_port = config.get(section='encoder', option ='port_com')
    boundrate = config.getint(section='encoder', option ='boundrate')
    stepper_motor_steps = config.getint(section='encoder', option = 'stepper_motor_steps')


except  Exception as f:
    print(f'Is not possible open file {f}')












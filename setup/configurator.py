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
    board_1 = config.getint(section='jlink_sn', option = 'board_1')
    jlink_path = config.get(section = 'jlink', option = 'path')
    arduino_nano_com_port = config.get(section='arduino', option='nano_port_com')
    arduino_nano_boudrate = config.get(section='arduino', option='nano_baudrate')
    arduino_nano_flash_path = config.get(section='arduino', option='nano_load_file')
    arduino_nano_erase = config.get(section='arduino', option='nano_erase_path')
    arduino_cli = config.get(section='arduino', option='cli')


except  Exception as f:
    print(f'Is not possible open file {f}')












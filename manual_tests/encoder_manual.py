from automated_tests.encoder.conftest import module_data
from automated_tests.encoder.map import StartUp
from tools.encoder.tools_encoder_handling import Commands

initialize_module = module_data()

def check_position(initialize_mode: StartUp):
    pos1 = initialize_mode.encoder.execute_measurement_in_percentage(cmd=Commands.ReadPosition,
                                               valve_steps=200)

    pass

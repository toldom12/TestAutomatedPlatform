from pathlib import Path

from automated_tests.encoder.map import StartUp
from tools.encoder.tools_encoder_handling import Commands
from tools.encoder.tools_encoder_handling import EncoderHandling
from setup.configurator import com_port, boundrate
from serial.serialutil import PARITY_NONE
from serial.serialutil import SerialException

try:
    initialize_module = StartUp(encoder=EncoderHandling(port=com_port,
                                                      parity=PARITY_NONE,
                                                      boundrate=boundrate))
except SerialException as e:
    print(f"Could not open serial port '{com_port}': {e}")
    raise SystemExit(1)

def check_position(initialize_mode: StartUp):
    pos1 = initialize_mode.encoder.execute_measurement_in_percentage(
        cmd=Commands.ReadPosition,
        valve_steps=200,
    )

if __name__ == '__main__':
    check_position(initialize_mode=initialize_module)

from dataclasses import dataclass

from tools.arduino.arduino import Arduino


@dataclass
class StartUp:
    arduino_nano : Arduino
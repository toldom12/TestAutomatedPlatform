from enum import StrEnum



class ArduinoCommand(StrEnum):
    STATUS = "STATUS"
    TEMP = "TEMP"
    NONE = "NONE"
    SELFTEST = "SELFTEST"


# class ArduinoHandling:
#     @staticmethod
#     def send_request(command: ArduinoCommand,
#                      module_data : StartUp):
#         pass

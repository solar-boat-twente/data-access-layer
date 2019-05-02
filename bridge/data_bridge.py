from threading import Thread

import config
from bridge.data_interpreter import DataInterpreter
from inputs.control_data_input import ControlDataInputDef
from inputs.telemetry_input_input import TelemetryInputInputDef
from inputs.user_power_input import UserPowerInputDef


class DataBridge:

    def __init__(self):
        self.__pipes = {
            config.pipe_control_data: DataInterpreter(ControlDataInputDef),
            config.pipe_telemetry_input: DataInterpreter(TelemetryInputInputDef),
            config.pipe_user_power: DataInterpreter(UserPowerInputDef)
        }

    def open_pipes(self):
        for path, interpreter in self.__pipes.items():
            pipe = DataPipe(path, interpreter)
            pipe.start()


class DataPipe(Thread):

    def __init__(self, path: str, interpreter: DataInterpreter):
        super().__init__()
        self.path = path
        self.interpreter = interpreter
        self.daemon = True

    def run(self):
        while True:
            with open(self.path, 'r') as file:
                for line in file:
                    if not line or not line.strip():
                        continue

                    self.interpreter.interpret(line)


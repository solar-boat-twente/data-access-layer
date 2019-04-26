from threading import Thread
from config import config
from bridge.data_interpreter import DataInterpreter
from inputs.control_data_input import ControlDataInterpreter, ControlDataInputDef
from inputs.user_power_input import UserPowerInputDef, UserPowerInputInterpreter


class DataBridge:

    def __init__(self):
        self.__pipes = {
            #'/home/ronaldboon/NetBeansProjects/Logging/pipes/UserPowerToPython': UserPowerInputInterpreter(UserPowerInputDef),
            config.PATH_TO_CONTROL_DATA_PIPE: ControlDataInterpreter(ControlDataInputDef)
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


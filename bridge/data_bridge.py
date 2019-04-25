from threading import Thread

from bridge.data_interpreter import DataInterpreter
from inputs.power_input import PowerInputInterpreter, PowerInputDef


class DataBridge:

    def __init__(self):
        self.__pipes = {
            'power_input.txt': PowerInputInterpreter(PowerInputDef)
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
        with open(self.path, 'r') as file:
            for line in file:
                if not line or not line.strip():
                    continue

                self.interpreter.interpret(line)


from typing import Union

from pyModbusTCP.server import ModbusServer, DataBank


class ModbusInstance:

    def __init__(self, host: str ='0.0.0.0', port: int = 502):
        self.port = port
        self.host = host
        self.server = None

    def run(self, run_async: bool = True):
        self.server = ModbusServer(host=self.host, port=self.port, no_block=run_async)
        self.server.start()

    @staticmethod
    def write_str(index: int, string: str):
        ModbusInstance.write(index, [ord(c) for c in string])

    @staticmethod
    def write_num(index: int, value: Union[int, float]):
        ModbusInstance.write(index, [value])

    @staticmethod
    def write(index: int, value: any):
        DataBank.set_words(index, value)

        index = index + 40001
        value = value[0] if isinstance(value, list) else value

        print('[Modbus] Wrote %s to index %s' % (value, index))


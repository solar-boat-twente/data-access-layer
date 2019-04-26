from typing import Union

from pyModbusTCP.server import ModbusServer, DataBank

from util.util_logging import log


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
        parsed_text = [ord(c) for c in string]
        ModbusInstance.write(index, parsed_text)

    @staticmethod
    def write_num(index: int, value: Union[int, float]):
        ModbusInstance.write(index, [value])

    @staticmethod
    def write_bit(index: int, value: int):
        DataBank.set_bits(index, [value])
        index += 10001
        log('[Modbus] Wrote %s to index %s' % (value, index))

    @staticmethod
    def write(index: int, value: any):
        index = index - 40001 if index > 40000 else index
        DataBank.set_words(index, value)

        value = value[0] if isinstance(value, list) else value
        index += 40001

        log('[Modbus] Wrote %s to index %s' % (value, index))


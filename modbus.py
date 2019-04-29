import struct

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
    def write_int(index: int, value: int):
        ModbusInstance.write(index, [value])

    @staticmethod
    def write_float(index: int, value: float):
        val = str(value).split('.')
        prefix = val[0]
        suffix = val[1]
        suffix = suffix+'0' if len(suffix) == 1 else suffix

        ModbusInstance.write(index, [int('%s%s' % (prefix, suffix))])

    @staticmethod
    def write_bit(index: int, value: int):
        DataBank.set_bits(index, [value])
        log('Wrote %s to index %s' % (value, index+10001))

    @staticmethod
    def write(index: int, value: any):
        index = index - 40001 if index > 40000 else index
        DataBank.set_words(index, value)

        value = value[0] if isinstance(value, list) else value
        index += 40001

        log('Wrote %s to index %s' % (value, index))


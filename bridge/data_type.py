from enum import Enum

from util.util_data_parser import parse_int, parse_float, parse_array


class DataType(Enum):

    string = (None, 'write_str')
    int = (parse_int, 'write_num')
    float = (parse_float, 'write_num')
    bit = (parse_int, 'write_bit')
    array = (parse_array, None)

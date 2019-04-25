def __ignore_exception(ignorable_exception=Exception, default_val=None):
    def dec(func):
        def _dec(*args, **kwargs):
            # noinspection PyBroadException
            try:
                return func(*args, **kwargs)
            except ignorable_exception:
                return default_val
        return _dec
    return dec


def parse_int(raw: str):
    s_int = __ignore_exception(ValueError)(int)
    return s_int(raw)


def parse_float(raw: str):
    s_float = __ignore_exception(ValueError)(float)
    return s_float(raw)


def parse_array(raw: str):
    return raw


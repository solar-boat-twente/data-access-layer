import collections


# noinspection PyUnresolvedReferences,PyProtectedMember
def nullable_namedtuple(typename, field_names, default_values=()):
    T = collections.namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, collections.Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T


Input = nullable_namedtuple('Input', 'index type modbus_ref default')
Output = nullable_namedtuple('Output', 'type modbus_ref')

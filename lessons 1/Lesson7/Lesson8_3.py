def adder(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for kwarg in kwargs:
        result += kwarg
    return result
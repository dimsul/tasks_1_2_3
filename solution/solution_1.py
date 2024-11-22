
def strict(func):
    def function(*args):
        types = [func.__annotations__[i] for i in func.__annotations__ if i != 'return']
        if len(args) != func.__code__.co_argcount:
            raise TypeError(f'function takes {func.__code__.co_argcount} positional arguments but {len(args)} were given')
        for i in range(len(args)):
            if type(args[i]) is not types[i]:
                raise TypeError(f'function takes {types[i]} argument but {type(args[i])} were given')
        result = func(*args)
        return result

    return function

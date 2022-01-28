from functools import wraps
from time import time


def stopwatch(f):
    """ 
    Decorator that measures function execution time.
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time()
        result = f(*args, **kwargs)
        te = time()
        print(f"'{f.__name__}' function execution time is {(te-ts):.4f} sec")
        return result
    return wrap

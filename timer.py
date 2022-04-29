from time import perf_counter
from typing import Callable


def timer(func: Callable) -> Callable:
    def f(*args, **kwargs):
        before = perf_counter()
        rv = func(*args, **kwargs)
        after = perf_counter()
        print(f"Time elapsed {after-before} s")
        return rv
    return f

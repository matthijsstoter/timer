from time import time
from typing import Callable


def timer(func: Callable) -> Callable:
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print(f"Time elapsed {after-before} s")
        return rv
    return f


def example():

    @timer
    def add(x: int, y: int = 10) -> float:
        return x + y

    add(x=10)

if __name__ == "__main__":
    example()
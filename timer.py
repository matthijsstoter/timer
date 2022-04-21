from time import time
from typing import Callable


def timer(func: Callable):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print(f"Time elapsed {after-before} s")
        return rv
    return f


def main():

    @timer
    def add(x: int, y: int = 10):
        return x + y

    add(x=10)

if __name__ == "__main__":
    main()
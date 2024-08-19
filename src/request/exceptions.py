from typing import Callable


def pathError(fn: Callable):
    def wrapper():
        try:
            fn()
        except:
            print()

    return wrapper

from typing import Callable
import configparser
import os


def pathError(fn: Callable):
    def wrapper():
        try:
            fn()
        except os.error:
            print("Error: Config file missing")

    return wrapper


def parsingError(fn: Callable):
    def wrapper():
        try:
            fn()
        except configparser.Error:
            print("Error: Config Integrity. check config.ini")

    return wrapper

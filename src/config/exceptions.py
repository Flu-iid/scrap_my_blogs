from typing import Callable
import configparser
import os


def pathError(fn: Callable):
    def wrapper():
        result = fn()
        if not result:
            print("Error: Path Error.config file missing")
        return result

    return wrapper


def parsingError(fn: Callable):
    def wrapper():
        try:
            return fn()
        except configparser.Error:
            print("Error: Parsing Error. check config rules")

    return wrapper


def configValueError(fn: Callable):
    def wrapper():
        try:
            fn()
            return True
        except configparser.Error:
            print("Error: Config Value Error. check config name and values")
            return False

    return wrapper

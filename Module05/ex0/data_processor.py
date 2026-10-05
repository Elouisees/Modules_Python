#!/usr/bin/env python3

import abc
from typing import Any, cast

# base class defines what must exist
# sublcasses defines how it works


class DataProcessor(abc.ABC):  # defines common processing interface
    # dont store self._storage here, bc subclass loses
    # flexibility to change how they store data
    def __init__(self) -> None:
        self._storage: list[tuple[int, Any]] = []
        self.index = 0

    @abc.abstractmethod  # provides template
    def validate(self, data: Any) -> bool:
        pass  # forces subclasses to implement method

    @abc.abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        extract = self._storage[0]
        self._storage.pop(0)
        return (extract)


# each specialized class will need to override methods
class NumericProcessor(DataProcessor):  # defines storage and behaviour
    # setting up initial values of an objects attributes
    # true when a class needs to maintain internal data over time
    # attribute exist before any method tries to use it
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):  # check for list
            for value in data:
                if type(value) not in (int, float):
                    # check elements inside list
                    return False
            return True
        elif type(data) is int or type(data) is float:  # check type
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        try:
            if not self.validate(data):
                raise ValueError
            elif isinstance(data, list):
                for item in data:
                    self._storage.append((self.index, item))
                    self.index += 1
            else:
                self._storage.append((self.index, data))
                self.index += 1
        except Exception:
            print("Got exception: Improper numeric data")


class TextProcessor(DataProcessor):  # defines storage and behaviour
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for value in data:
                if type(value) is not str:
                    return False
            return True
        elif isinstance(data, str):
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        try:
            if not self.validate(data):
                raise ValueError
            elif isinstance(data, list):
                for item in data:
                    self._storage.append((self.index, item))
                    self.index += 1
            else:
                self._storage.append((self.index, data))
                self.index += 1
        except Exception:
            print("Got exception: Improper alpabetic data")


class LogProcessor(DataProcessor):  # defines storage and behaviour
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for i in data:
                if type(i) is dict:
                    for key, value in i.items():
                        if type(key) is not str or type(value) is not str:
                            return False
                else:
                    return False
            return True
        elif isinstance(data, dict):
            for key, value in data.items():
                if type(key) is not str or type(value) is not str:
                    return False
            return True
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        try:
            if not self.validate(data):
                raise ValueError
            elif isinstance(data, list):
                for item in data:
                    self._storage.append((self.index, item))
                    self.index += 1
            else:
                self._storage.append((self.index, data))
                self.index += 1
        except Exception:
            print("Got exception: Improper alphabetic data"
                  "(within dictionary)")


def print_log(dict_str: str) -> str:
    log_dict: dict[str, str] = cast(dict[str, str], dict_str)

    val_list: list[str] = []
    for key, value in log_dict.items():
        val_list.append(value)

    string: str = ": ".join(val_list)
    return string


# a specialized class is a user-defined class
# that extends or customizes
# bahviour of a more general class (DataProcessor) by
# adding/overriding methods/attributes

num = NumericProcessor()
text = TextProcessor()
log = LogProcessor()

# if __name__ == "__main__":
#     print(num.validate([1, 2, 3, 4, 5]))
#     num.ingest([1, 2, 3, 4, 5])
#     num_discard_one = num.output()
#     print(f"Numeric Value {num_discard_one[0]}: {num_discard_one[1]}")

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    # ---------------------------------------------------------- NUMERIC TESTS
    print("---- Testing Numeric Processor ----\n")
    print(f"Trying to validate input '42': {num.validate(42)}")
    print(f"Trying to validate input 'True': {num.validate(True)}")
    print(f"Trying to validate input 'Hello': {num.validate('hello')}")
    print(f"Trying to validate input '[42, 89.0]': {num.validate([42, 89.0])}")
    print("Trying to validate input '[42, \"hello\"]':"
          f"{num.validate([42, 'hello'])}")

    print("\nTest invalid ingestion without prior validation:")
    num.ingest("foo")  # invalid input -> mypy error
    num.ingest([1, 2, 3, 4, 5])

    num_discard_one = num.output()
    num_discard_two = num.output()
    num_discard_three = num.output()
    print("\nExtracting 3 values...")
    print(f"Numeric value {num_discard_one[0]}: {num_discard_one[1]}")
    print(f"Numeric value {num_discard_two[0]}: {num_discard_two[1]}")
    print(f"Numeric value {num_discard_three[0]}: {num_discard_three[1]}")
    print("\n----------------------------------")

    # ------------------------------------------------------------- TEXT TESTS
    print("\n---- Testing Text Processor ----\n")
    print(f"Trying to validate input '42': {text.validate(42)}")
    print(f"Trying to validate input 'hello': {text.validate('hello')}")
    print("Trying to validate input '[Hello, World]':"
          f"{text.validate(['Hello', 'world'])}")
    print("Trying to validate input '[42, hello]':"
          f"{text.validate([42, 'hello'])}")

    print("\nTest invalid ingestion without prior validation:")
    text.ingest(42)  # invalid input -> mypy error
    text.ingest(["hello", "world"])

    text_discard_one = text.output()
    print("\nExtracting 1 value...")
    print(f"Text value {text_discard_one[0]}: {text_discard_one[1]}")
    print("\n----------------------------------")

    # ---------------------------------------------------------- LOG/DICT TESTS
    list_of_dic = [{"log_level": "NOTICE"}, {"log_message": "Hello, world"}]
    print("\n---- Testing Log Processor ----\n")
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    print("Trying to validate input 'log_level: NOTICE':"
          f"{log.validate(list_of_dic)}")
    print(f"Trying to validate input '\"log_message\": 42': "
          f"{log.validate({'log_message': 42})}")
    print(f"Trying to validate input '42': {log.validate(42)}")
    print("Trying to validate input '\"log_message\": \"hello,world\"': "
          f"{log.validate({'log_message': 'hello, world'})}")
    print("Test invalid ingestion without prior validation:")

    list_of_dic2 = [{"log_level": "NOTICE", "log_message":
                     "Connection to server"}, {"log_level": "ERROR",
                                               "log_message":
                                               "Unauthorized access!!"}]
    print("\nTest invalid ingestion without prior validation:")
    log.ingest(42)  # invalid input -> mypy error
    log.ingest(list_of_dic2)

    log_discard_one = log.output()
    str1 = print_log(log_discard_one[1])
    log_discard_two = log.output()
    str2 = print_log(log_discard_two[1])
    print("\nExtracting 2 values...")
    print(f"Log entry {log_discard_one[0]}: {str1}")
    print(f"Log entry {log_discard_two[0]}: {str2}")
    print("\n----------------------------------")

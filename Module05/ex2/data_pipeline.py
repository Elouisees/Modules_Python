#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol

# base class defines what must exist
# sublcasses defines how it works


class DataProcessor(ABC):  # defines common processing interface
    # dont store self._storage here, bc subclass loses
    # flexibility to change how they store data
    def __init__(self) -> None:
        self._storage: list[tuple[int, Any]] = []
        self._index = 0
        self._processed = 0

    @abstractmethod  # provides template
    def validate(self, data: Any) -> bool:
        pass  # forces subclasses to implement method

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        try:
            extract = self._storage[0]
            self._storage.pop(0)
            return (extract)
        except Exception:
            raise Exception


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
                    self._storage.append((self._index, item))
                    self._index += 1
            else:
                self._storage.append((self._index, data))
                self._index += 1
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
                    self._storage.append((self._index, item))
                    self._index += 1
            else:
                self._storage.append((self._index, data))
                self._index += 1
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
                    self._storage.append((self._index, item))
                    self._index += 1
            else:
                self._storage.append((self._index, data))
                self._index += 1
        except Exception:
            print("Got exception: Improper alphabetic data"
                  "(within dictionary)")

    # protocol allows to define structural types (duck typing
    # -> class has right methods, automatically matches protocol

    # why protocol instead of abc class?
    # -> abc forces inheritence, protocol enforces structure


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if len(data) != 0:
            print("CSV Output:")
            csv_output: str = ""
            for item in data:
                if isinstance(item[1], dict):
                    for key, value in item[1].items():
                        csv_output += f"{key}: {value},"
                else:
                    csv_output += f"{item[1]},"
            csv_output = csv_output[:-1]
            print(csv_output)


class JSONPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if len(data) != 0:
            print("JSON Output:")
            json_output: str = "{"
            for item in data:
                json_output += f"\"item_{item[0]}:\""
                if isinstance(item[1], dict):
                    for key, value in item[1].items():
                        json_output += f" \"{key}: {value}\","
                else:
                    json_output += f" \"{item[1]}\", "
            json_output = json_output[:-1]
            json_output += "}"
            print(json_output)


# a specialized class is a user-defined class that extends
# or customizes
# bahviour of a more general class (DataProcessor) by
# adding/overriding methods/attributes

class Datastream():
    # receive data of different types, sends data to appropriate processor
    def __init__(self) -> None:
        self._listproc: list[DataProcessor] = []
        self._elems_left = 0

    def register_processor(self, proc: DataProcessor | None) -> None:
        try:
            if isinstance(proc, DataProcessor):
                self._listproc.append(proc)
                print(f"Registering {proc.__class__.__name__}\n")
                # proc is instance, does not have a name
            else:
                raise ValueError
        except Exception:
            print("No processor found, no data\n")

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            sign: int = 0
            if isinstance(item, list):
                for that_item in item:
                    for proc in self._listproc:
                        if proc.validate(that_item):
                            proc.ingest(that_item)
                            sign = 1
            else:
                for proc in self._listproc:
                    if proc.validate(item):
                        proc.ingest(item)
                        sign = 1
            if sign == 0:
                print("Datastream error - Can't process element in stream:"
                      f" {item}")

    def print_processors_stats(self) -> None:
        for proc in self._listproc:
            if isinstance(proc, NumericProcessor):
                remain = len(proc._storage)
                print(
                    f"Numeric Processor: total {proc._index} items "
                    f"processed, remaining {remain} on processor\n"
                )
            elif isinstance(proc, TextProcessor):
                remain = len(proc._storage)
                print(
                    f"Text Processor: total {proc._index} items "
                    f"processed, remaining {remain} on processor\n"
                )
            elif isinstance(proc, LogProcessor):
                remain = len(proc._storage)
                print(
                    f"Log Processor: total {proc._index} items "
                    f"processed, remaining {remain} on processor\n"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if isinstance(plugin, (CSVPlugin, JSONPlugin)):
            for proc in self._listproc:
                try:
                    collect_export: list[tuple[int, str]] = []
                    i: int = 0
                    while i in range(nb):
                        item = proc.output()
                        if item is not None:
                            collect_export.append(item)
                        i += 1
                    # print(collect_export)
                    plugin.process_output(collect_export)
                except Exception:
                    # print(collect_export)
                    plugin.process_output(collect_export)
                    continue
        else:
            raise ValueError("Incompatible ExportPlugin")


num = NumericProcessor()
txt = TextProcessor()
log = LogProcessor()

test = Datastream()
data = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
        {'log_level': 'NOTICE', 'log_message':
         'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello']
test_data = ["hello, world", [3.14, -1, 2.71],
             [{"log-level": "WARNING", "log_message":
               "Telnet acces! Use ssh instead"},
             {"log_level": "INFO", "log_message": "User wil is connected"}],
             42, ["Hi", "Five"]]


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")

    print("== DataStream statistics ==")
    test.register_processor(None)
    print("Registering Processors:")
    test.register_processor(num)
    test.register_processor(txt)
    test.register_processor(log)

    print("Send first batch on data stream:", test_data)
    test.process_stream(test_data)

    print("\n== DataStream statistics ==")
    test.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    test.output_pipeline(3, CSVPlugin())

    print("Send another batch of data:", data)
    test.process_stream(data)

    print("== DataStream statistics ==")
    test.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    test.output_pipeline(5, JSONPlugin())

    print("== DataStream statistics ==")
    test.print_processors_stats()

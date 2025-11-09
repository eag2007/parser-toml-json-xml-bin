import time
import tracemalloc
import os
import json
import toml 

from parse_json import *
from parse_toml import *
from automatic_parse import *


def test1():

    tracemalloc.start()
    start_time = time.time()

    read_to_toml_for_python = read_to_toml('./toml_folder/source.toml')
    toml_to_python = toml_parse_to_python(read_to_toml_for_python)
    python_to_json = convert_to_json(toml_to_python)
    write_to_json_for_python = python_parse_to_json(python_to_json, './json_folder/source.json')

    end_time = time.time()

    delta_time = end_time - start_time

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Разница во времени при моем решение: ", delta_time)
    print("Разница в памяти при моем решение (среднее, максимум): ", current, peak)


def test2():
    tracemalloc.start()
    start_time = time.time()

    read_toml = deserialize()
    write_json = serialize(read_toml)

    end_time = time.time()

    delta_time = end_time - start_time

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Разница во времени при решении через библиотеки: ", delta_time)
    print("Разница в памяти при решении через библиотеки (среднее, максимум): ", current, peak)
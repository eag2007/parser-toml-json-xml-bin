from parse_toml import toml_parse_to_python, read_to_toml
from parse_json import python_parse_to_json, convert_to_json
from parse_xml import convert_to_xml, python_parse_to_xml
from parse_bin import parse_to_bin, parse_to_python
from pprint import pprint
from automatic_parse import deserialize, serialize
from test import test1, test2


if __name__ == "__main__":
    print(502010 % 132)


    print()
    print("Задания 1")

    read_to_toml_for_python = read_to_toml('./toml_folder/source.toml')
    toml_to_python = toml_parse_to_python(read_to_toml_for_python)
    toml_to_python_to_bin = parse_to_bin(toml_to_python)
    print("Перевод в бинарный тип: (Десериализация)", type(toml_to_python_to_bin))
    print(toml_to_python_to_bin)

    bin_to_python = parse_to_python()
    python_to_json = convert_to_json(toml_to_python)
    write_to_json_for_python = python_parse_to_json(python_to_json, './json_folder/source.json')
    print("Перевод в python объекты: (Сереализация)", type(bin_to_python))


    print()
    print("Задание 2")
    read_toml = deserialize()
    print(read_toml == toml_to_python)
    # Мой парсер и библиотека одинаково считывает toml
    write_json = serialize(read_toml)
    print(write_json == python_to_json)
    # Мой парсер записывает json в более красивом и читаемом формате, а также отображает русские символы


    print()
    print("Задание 3")
    python_to_xml = convert_to_xml(toml_to_python)
    write_to_xml_for_python = python_parse_to_xml(python_to_xml, './xml_folder/source.xml')


    print()
    print("Задание 4")
    test1()
    test2()
    # Мое решение работает быстрее и требует меньше памяти на пике, но больше памяти в среднем, 
    # возможно это потому что библиотеки рассматривают больше случаев
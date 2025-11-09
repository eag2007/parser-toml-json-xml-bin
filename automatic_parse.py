import json
import toml 


def deserialize():
    with open('./toml_folder/source.toml', 'r', encoding='utf-8') as f:
        python_object = toml.load(f)
    return python_object


def serialize(value):
    with open('./json_folder/data.json', 'w', encoding='UTF-8') as w:
        json.dump(value, w)
    with open('./json_folder/data.json', 'r', encoding='UTF-8') as f:
        json_serialize = f.read()
    return json_serialize
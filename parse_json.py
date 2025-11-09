
def python_parse_to_json(value, filename):
    # result = convert_to_json(value)

    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(value)

    print(f"Даннные загружены")


def convert_to_string(s):
    s = str(s)
    result = ''
    for i in s:
        if i == '"':
            result += '\\"'
        elif i == '\\':
            result += '\\\\'
        elif i == '\n':
            result += '\\n'
        elif i == '\r':
            result += '\\r'
        elif i == '\t':
            result += '\\t'
        else:
            result += str(i)
    return result


def convert_to_json(data, count=0):
    delta = '    ' * count
    if data is None:
        return 'null'
    if isinstance(data, bool):
        if data:
            return 'true'
        return 'false'
    if isinstance(data, int):
        return f'"{str(data)}"'
    if isinstance(data, float):
        return f'"{str(data)}"'
    if isinstance(data, str):
        return f'"{convert_to_string(data)}"'
    if isinstance(data, list):
        if not data:
            return '[]'
        container = []
        for element in data:
            element = convert_to_json(element, count + 1)
            container.append(f'{delta}    {element}')
        return f'[\n{",\n".join((container))}\n{delta}]'
    if isinstance(data, dict):
        if not data:
            return '{}'
        container = []
        for key, val in data.items():
            key_ = convert_to_string(key)
            val_ = convert_to_json(val, count + 1)
            container.append(f'{delta}    "{key_}": {val_}')
        return '{\n' + ',\n'.join(container) + '\n' + str(delta) + '}'
    return convert_to_string(str(data))

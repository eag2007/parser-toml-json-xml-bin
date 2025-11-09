def convert_to_type(value):
    if 'true' in value:
        return True
    if 'false' in value:
        return False
    if value.count('"') == 2:
        return value[value.find('"') + 1:value.rfind('"')]
    if value.isdigit():
        return int(value)
    if value.replace('.', '', 1).replace(' ', '').isdigit():
        return float(value.replace(' ', ''))
    return value
    

def read_to_toml(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.read()
    return lines
    

def toml_parse_to_python(lines: str):
    lines = lines.splitlines()

    print("Данные считаны")

    result = {}
    table_value = None

    for line in lines:
        if not line:
            continue

        if line.startswith('[[') and line.endswith(']]'):
            names = line.replace(' ', '')[2:-2].split('.')

            container = result
            for name in names[:-1]:
                if name not in container.keys():
                    container[name] = {}
                container = container[name]

            if names[-1] not in container.keys():
                container[names[-1]] = []

            table_value = {}
            container[names[-1]].append(table_value)
        elif line.startswith('[') and line.endswith(']'):
            names = line.replace(' ', '')[1:-1].split('.')

            container = result
            for name in names[:-1]:
                if name not in container.keys():
                    container[name] = {}
                container = container[name]

            if names[-1] not in container.keys():
                container[names[-1]] = {}
            
            table_value = container[names[-1]]
        elif '=' in line and table_value is not None:
            key, value = line.split('=')
            key = key.strip()
            value = convert_to_type(value)
            table_value[key] = value
    return result
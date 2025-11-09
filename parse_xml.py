def convert_to_string(s):
    s = str(s)
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    s = s.replace('"', '&quot;').replace("'", '&apos;')
    return s


def convert_to_xml(data, tag='main', count=0):
    delta= '    ' * count
    if data is None:
        return f'{delta}<{tag}>null</{tag}>'
    if isinstance(data, bool):
        if data:
            return f'{delta}<{tag}>true</{tag}>'
        return f'{delta}<{tag}>false</{tag}>'
    if isinstance(data, int):
        return f'{delta}<{tag}>{str(data)}</{tag}>'
    if isinstance(data, float):
        return f'{delta}<{tag}>{str(data)}</{tag}>'
    if isinstance(data, str):
        return f'{delta}<{tag}>{convert_to_string(data)}</{tag}>'
    if isinstance(data, list):
        if not data:
            return f'{delta}<{tag}></{tag}>'

        result = f'{delta}<{tag}>'
        for element in data:
            if tag[-1] == 's':
                tag_name = tag[:-1]
            else:
                tag_name = 'element'
            result += f'\n{convert_to_xml(element, tag_name, count + 1)}'
        result += f'\n{delta}</{tag}>'
        return result
    if isinstance(data, dict):
        if not data:
            return f'{delta}<{tag}></{tag}>'
        
        result = f'{delta}<{tag}>'
        for key, value in data.items():
            tag_name = str(key)
            if tag_name and tag_name[0].isdigit():
                tag_name = f'element_{tag_name}'
            tag_name = tag_name.replace('_', '').replace('-', '')
            if not tag_name or tag_name[0].isdigit():
                tag_name = f'element_{tag_name}'
                
            result += f'\n{convert_to_xml(data[key], tag_name, count + 1)}'
        result += f'\n{delta}</{tag}>'
        return result
    return f'{delta}<{tag}>{convert_to_string(str(data))}</{tag}>'


def python_parse_to_xml(data, filename):
    with open(filename, 'w', encoding='UTF-8') as f:
        print(f'<?xml version="1.0" encoding="UTF-8"?>', file=f)
        f.write(data)

    print("Данные загружены в xml")
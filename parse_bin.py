import struct
from parse_toml import read_to_toml, toml_parse_to_python

def convert_to_bin_type(data):
    if isinstance(data, str):
        encoded = data.encode('UTF-8')
        return b'\x00' + struct.pack('>I', len(encoded)) + encoded
    elif isinstance(data, int):
        return b'\x01' + struct.pack('>q', data)
    elif isinstance(data, bool):
        if data:
            return b'\x03\x01'
        return b'\x03\x00'
    elif isinstance(data, float):
        return b'\x02' + struct.pack('>d', data)
    elif data is None:
        return b'\x04'
    elif isinstance(data, list):
        result = b'\x05' + struct.pack('>I', len(data))
        for i in data:
            result += parse_to_bin(i)
        return result
    elif isinstance(data, dict):
        result = b'\x06' + struct.pack('>I', len(data))
        for key, value in data.items():
            result += parse_to_bin(str(key))
            result += parse_to_bin(value)
        return result


def convert_to_python_type(data, offset):
    type_value = data[offset]
    if type_value == 0:
        offset += 1
        length = struct.unpack_from('>I', data, offset)[0]
        offset += 4
        value = data[offset:offset + length]
        offset += length
        return value.decode('UTF-8'), offset
    
    if type_value == 1:  # int
        offset += 1
        value = struct.unpack_from('>q', data, offset)[0]
        return value, offset + 8
    
    if type_value == 2:  # float
        offset += 1
        value = struct.unpack_from('>d', data, offset)[0]
        return value, offset + 8
    
    if type_value == 3:  # bool
        offset += 1
        value = data[offset] == 1
        return value, offset + 1
    
    if type_value == 4:  # None
        return None, offset + 1
    
    if type_value == 5:  # list
        offset += 1
        length = struct.unpack_from('>I', data, offset)[0]
        offset += 4
        result = []
        for i in range(length):
            element, offset = convert_to_python_type(data, offset)
            result.append(element)
        return result, offset
    
    if type_value == 6:  # dict
        offset += 1
        length = struct.unpack_from('>I', data, offset)[0]
        offset += 4
        result = {}
        for i in range(length):
            key, offset = convert_to_python_type(data, offset)
            key = str(key)
            value, offset = convert_to_python_type(data, offset)
            result[key] = value
        return result, offset


def parse_to_bin(data):
    binary_data = convert_to_bin_type(data)
    with open('./bin_folder/source.bin', 'wb') as f:
        f.write(binary_data)
    return binary_data


def parse_to_python():
    with open('./bin_folder/source.bin', 'rb') as f:
        binary_data = f.read()
    result, offset = convert_to_python_type(binary_data, 0)
    return result
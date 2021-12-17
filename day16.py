from typing import List, Dict

INPUT_FILE = "input-day16.txt"


def get_lines(filename: str) -> List:
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def literal_packet(packet: str, pos: int, attributes: Dict):
    value = ""
    done = False
    while not done:
        if packet[pos] == '0':
            done = True
        pos += 1
        value += packet[pos:pos+4]
        pos += 4
    # print(f"{value=}")
    value_list = attributes.get('values', [])
    value_list.append(int(value,2))
    attributes['values'] = value_list
    return pos


def operator_packet(packet: str, pos: int, attributes: Dict):
    length_type = packet[pos]
    # print(f"{length_type=}")
    pos += 1
    if length_type == '0':
        subpacket_length = packet[pos:pos+15]
        # print(f"{subpacket_length=}")
        pos += 15
        end = pos + int(subpacket_length, 2)
        while pos < end:
            pos = process_packet(packet, pos, attributes)
    else:
        subpacket_count = packet[pos:pos+11]
        # print(f"{subpacket_count=}")
        pos += 11
        count = 0
        while count < int(subpacket_count, 2):
            pos = process_packet(packet, pos, attributes)
            count += 1
    return pos


def prod(values: List) -> int:
    result = 1
    for i in values:
        result *= i
    return result


def process_packet(packet: str, pos: int, attributes: Dict):
    packet_version = packet[pos:pos+3]
    attributes['version_sum'] = attributes.get(
        'version_sum', 0) + int(packet_version, 2)
    # print(f"{packet_version=}")
    pos += 3
    packet_type = packet[pos:pos+3]
    # print(f"{packet_type=}")
    pos += 3
    if int(packet_type, 2) == 4:
        pos = literal_packet(packet, pos, attributes)
    else:
        if 'values' in attributes:
            temp = [value for value in attributes['values']]
        else:
            temp = []
        attributes['values'] = []
        pos = operator_packet(packet, pos, attributes)
        #print(f"{attributes['values']=}")
        if int(packet_type, 2) == 0:
            result = sum(attributes['values'])
        elif int(packet_type, 2) == 1:
            result = prod(attributes['values'])
        elif int(packet_type, 2) == 2:
            result = min(attributes['values'])
        elif int(packet_type, 2) == 3:
            result = max(attributes['values'])
        elif int(packet_type, 2) == 5:
            result = 1 if attributes['values'][0] > attributes['values'][1] else 0
        elif int(packet_type, 2) == 6:
            result = 1 if attributes['values'][0] < attributes['values'][1] else 0
        elif int(packet_type, 2) == 7:
            result = 1 if attributes['values'][0] == attributes['values'][1] else 0
        temp.append(result)
        attributes['values'] = temp

    return pos


def get_binary(hex_string: str) -> str:
    binary = ""
    for c in hex_string:
        binary += "{0:04b}".format(int(c, 16))
    return binary


def part1():
    lines = get_lines(INPUT_FILE)
    hex_string = lines[0]
    packet = get_binary(hex_string)
    attributes = dict()
    pos = process_packet(packet, 0, attributes)
    print(attributes)
    return


def part2():
    lines = get_lines(INPUT_FILE)
    hex_string = lines[0]
    packet = get_binary(hex_string)
    attributes = dict()
    pos = process_packet(packet, 0, attributes)
    print(attributes)
    return


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

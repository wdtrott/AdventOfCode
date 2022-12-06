with open('/Users/wtrott/Downloads/input1206.txt') as file:
    data = file.read().replace('\n', '')

def find_marker(input_data: str, marker_size: int):
    for position in range(0, len(data) - (marker_size - 1)):
        block = set(data[position: marker_size + position])
        if len(block) == marker_size:
            print(f"Marker found after character {marker_size + position}")
            break

find_marker(data, 4)
find_marker(data, 14)

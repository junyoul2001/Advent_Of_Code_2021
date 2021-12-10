def prob1(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.split())

    pos, depth = 0, 0

    for i in input_array:
        if i[0] == "forward":
            pos += int(i[1])
        elif i[0] == "up":
            depth -= int(i[1])
        else:
            depth += int(i[1])

    return pos * depth

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.split())

    pos, depth, aim = 0, 0, 0

    for i in input_array:
        if i[0] == "forward":
            pos += int(i[1])
            depth += aim * int(i[1])
        elif i[0] == "up":
            aim -= int(i[1])
        else:
            aim += int(i[1])

    return pos * depth
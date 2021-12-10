def prob1(file):
    input = open(file, "r").readlines()
    temp = 0
    res = 0

    for line in input:
        if temp != 0 and temp < int(line):
            res += 1
        temp = int(line)

    return res

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []
    res = 0
    i = 3

    for line in input:
        input_array.append(int(line))

    while i < len(input_array):
        if input_array[i] + input_array[i-1] + input_array[i-2] > input_array[i-1] + input_array[i-2] + input_array[i-3]:
            res += 1
        i += 1

    return res

def prob1(file):
    input = open(file, "r").readlines()
    input_array = []
    crab_pos = []

    for line in input:
        input_array.append(line.strip().split(','))

    for str in input_array[0]:
        crab_pos.append(int(str))

    fuel = [0] * (max(crab_pos) + 1)
    for i in range(len(fuel)):
        for j in range(len(crab_pos)):
            fuel[i] += abs(crab_pos[j] - i)

    return min(fuel)

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []
    crab_pos = []

    for line in input:
        input_array.append(line.strip().split(','))

    for str in input_array[0]:
        crab_pos.append(int(str))

    fuel = [0] * (max(crab_pos) + 1)
    for i in range(len(fuel)):
        for j in range(len(crab_pos)):
            diff = abs(crab_pos[j] - i)
            fuel[i] += diff * (diff+1) // 2

    return min(fuel)
def prob1(file):
    input = open(file, "r").readlines()
    fishes_str = []
    fishes_int = []

    for line in input:
        fishes_str.append(line.strip().split(','))

    for fish in fishes_str[0]:
        fishes_int.append(int(fish))

    days = 80
    while days > 0:
        for i in range(len(fishes_int)):
            fishes_int[i] -= 1
            if fishes_int[i] < 0:
                fishes_int[i] = 6
                fishes_int.append(8)
        days -= 1

    return len(fishes_int)

def prob2(file):
    input = open(file, "r").readlines()
    fishes_str = []
    fish_count = [0] * 9

    for line in input:
        fishes_str.append(line.strip().split(','))

    for fish in fishes_str[0]:
        fish_count[int(fish)] += 1

    days = 256
    for _ in range(0, days):
        temp_count = fish_count.copy()
        for i in range(8, -1, -1):
            if i != 0:
                fish_count[i-1] = temp_count[i]
            else:
                fish_count[8] = temp_count[0]
                fish_count[6] += temp_count[0]

    return sum(fish_count)
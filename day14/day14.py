def prob1(file):
    input = open(file, "r").read().split('\n\n')

    polymer = input[0]
    template = [x.split(' -> ') for x in input[1].split('\n')]

    steps = 0
    letters = []
    while steps != 10:
        for i in range(0, (len(polymer)-1)*2, 2):
            letters.append(polymer[i]) if polymer[i] not in letters else letters
            letters.append(polymer[i+1]) if polymer[i+1] not in letters else letters

            pair = polymer[i] + polymer[i+1]
            for rule in template:
                if rule[0] == pair:
                    polymer = polymer[:i+1] + rule[1] + polymer[i+1:]
        steps += 1
    
    most = 0
    least = float('inf')
    for letter in letters:
        most = polymer.count(letter) if polymer.count(letter) > most else most
        least = polymer.count(letter) if polymer.count(letter) < least else least

    return most - least

def prob2(file):
    input = open(file, "r").read().split('\n\n')

    polymer = input[0]
    template = [x.split(' -> ') for x in input[1].split('\n')]

    steps = 0
    pair_count = {}
    letter_count = {}

    for pair in template:
        pair_count[pair[0]] = 0
        if pair[0][1] not in letter_count:
            letter_count[pair[0][0]] = 0 
        if pair[0][1] not in letter_count:
            letter_count[pair[0][1]] = 0    

    for i in range(0, len(polymer)-1):
        pair_count[polymer[i] + polymer[i+1]] += 1
        letter_count[polymer[i]] = 1 if i == 0 else 0
        letter_count[polymer[i+1]] += 1 

    while steps != 40:
        init_pair_count = pair_count.copy()
        for rule in template:
            pair, letter = rule
            init_count = init_pair_count[pair]

            if init_count == 0:
                continue

            new_pair_1 = pair[0] + letter
            new_pair_2 = letter + pair[1]

            pair_count[new_pair_1] += init_count
            pair_count[new_pair_2] += init_count
            pair_count[pair] -= init_count

            letter_count[letter] += init_count
        steps += 1

    most = 0
    least = float('inf')
    for count in letter_count.values():
        most = count if count > most else most
        least = count if count < least else least

    return most - least
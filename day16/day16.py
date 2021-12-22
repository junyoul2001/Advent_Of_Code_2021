import math

def hexa_to_binary(character):
    return bin(int(character, 16))[2:].zfill(4)

def binary_to_dec(character):
    return int(character, 2)

def evaluate_exp(id, vals):
    res = 0
    if id == 0:
        res = sum(vals)
    elif id == 1:
        res = math.prod(vals)
    elif id == 2:
        res = min(vals)
    elif id == 3:
        res = max(vals)
    elif id == 4:
        res = vals[0]
    elif id == 5:
        res = 1 if vals[0] > vals[1] else 0
    elif id == 6:
        res = 1 if vals[0] < vals[1] else 0
    elif id == 7:
        res = 1 if vals[0] == vals[1] else 0
        
    return res

def parse_packets(input, index):
    i = index
    final_ver = binary_to_dec(input[i:i+3])
    id = binary_to_dec(input[i+3:i+6])
    i += 6

    if id == 4:
        packet_val = [0] 
        while True:
            packet_val[0] = (16 * packet_val[0] + binary_to_dec(input[i+1:i+5]))
            i += 5
            if input[i-5] == '0':
                break
    else:
        packet_val = []
        if input[i] == '0':
            final_i = i + 16 + binary_to_dec(input[i+1:i+16])
            i += 16
            while i < final_i:
                i, new_ver, new_val = parse_packets(input, i)
                final_ver += new_ver
                packet_val.append(new_val)
        else:
            num_packets = binary_to_dec(input[i+1:i+12])
            i += 12
            for _ in range(num_packets):
                i, new_ver, new_val = parse_packets(input, i)
                final_ver += new_ver
                packet_val.append(new_val)

    return i, final_ver, evaluate_exp(id, packet_val)

def prob1(file):
    input = open(file, "r").readlines()

    for line in input:
        input_str = (hexa_to_binary(line.strip()))

    while len(input_str) % 4 != 0:
        input_str = '0' + input_str

    return parse_packets(input_str, 0)[1]

def prob2(file):
    input = open(file, "r").readlines()

    for line in input:
        input_str = (hexa_to_binary(line.strip()))

    while len(input_str) % 4 != 0:
        input_str = '0' + input_str

    return parse_packets(input_str, 0)[2]
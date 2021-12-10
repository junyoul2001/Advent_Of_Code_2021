def prob1(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.strip())

    gamma = [None] * len(input_array[0]) 
    epsilon = [None] * len(input_array[0])

    for bit in range(len(input_array[0])):    
        bit_array = [list[bit] for list in input_array]

        if bit_array.count('1') > bit_array.count('0'):
            gamma[bit] = '1'
            epsilon[bit] = '0'
        else:
            gamma[bit] = '0'
            epsilon[bit] = '1'

    gamma_dec = int(''.join(gamma), 2)
    epsilon_dec = int(''.join(epsilon), 2)

    return gamma_dec * epsilon_dec

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.strip())

    oxy_rate = co2_rate = input_array.copy()

    for bit in range(len(oxy_rate[0])):    
        oxy_bits = [list[bit] for list in oxy_rate]

        if oxy_bits.count('1') >= oxy_bits.count('0'):
            oxy_rate = [list for list in oxy_rate if list[bit] == '1']
        else:
            oxy_rate = [list for list in oxy_rate if list[bit] == '0']

        if len(oxy_rate) == 1:
            break

    for bit in range(len(co2_rate[0])):
        co2_bits = [list[bit] for list in co2_rate]

        if co2_bits.count('1') >= co2_bits.count('0'):
            co2_rate = [list for list in co2_rate if list[bit] == '0']
        else:
            co2_rate = [list for list in co2_rate if list[bit] == '1']
        
        if len(co2_rate) == 1:
            break

    oxy_dec = int(oxy_rate[0], 2)
    co2_dec = int(co2_rate[0], 2)
    
    return oxy_dec * co2_dec
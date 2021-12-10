def prob1(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.strip().split(' | '))

    seg_inputs = []
    seg_outputs= []
    for i in range(len(input_array)):
        seg_inputs.append(input_array[i][0].split())
        seg_outputs.append(input_array[i][1].split())

    unique_count = 0
    unique_len = {2,3,4,7}
    for seg in seg_outputs:
        for digit in seg:
            if len(digit) in unique_len:
                unique_count += 1

    return unique_count

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.strip().split(' | '))

    seg_inputs = []
    seg_outputs= []
    for i in range(len(input_array)):
        seg_inputs.append(input_array[i][0].split())
        seg_outputs.append(input_array[i][1].split())

    input_values = seg_inputs.copy()
    for i in range(len(seg_inputs)):
        sorted_seg = sorted(seg_inputs[i], key=len)
        n1 = sorted_seg[0] # cf
        n7 = sorted_seg[1] # cf a
        n4 = sorted_seg[2] # cf bd
        bd = [x for x in n4 if x not in n1]
        n8 = sorted_seg[9]
        for j in range(3, len(sorted_seg)-1):
            if len(sorted_seg[j]) == 5:
                if n1[0] in sorted_seg[j] and n1[1] in sorted_seg[j]:
                    n3 = sorted_seg[j]
                elif bd[0] in sorted_seg[j] and bd[1] in sorted_seg[j]:
                    n5 = sorted_seg[j]
                else:
                    n2 = sorted_seg[j]
            elif len(sorted_seg[j]) == 6:
                if n1[0] in sorted_seg[j] and n1[1] in sorted_seg[j] and bd[0] in sorted_seg[j] and bd[1] in sorted_seg[j]:
                    n9 = sorted_seg[j]
                elif bd[0] in sorted_seg[j] and bd[1] in sorted_seg[j]:
                    n6 = sorted_seg[j]
                else:
                    n0 = sorted_seg[j]
        input_values[i] = list(map("".join,(map(sorted, [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]))))

    output_digits = []
    for i in range(len(seg_outputs)):
        current_digit = ''
        for j in range(len(seg_outputs[i])):
            current_digit += str(input_values[i].index("".join(sorted(seg_outputs[i][j]))))
        output_digits.append(int(current_digit))
                
    return sum(output_digits)
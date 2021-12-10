def prob1(file):
    input = open(file, "r").readlines()
    input_array = []
    coord_array = []
    grid = [[0 for i in range(1000)] for j in range(1000)]

    for line in input:
        input_array.append(line.strip().split(' -> '))

    for i in range(len(input_array)):
        for j in range(len(input_array[i])):
            coord_array.append(input_array[i][j].split(','))

    for row in coord_array:
        for i in range(len(row)):
            row[i] = int(row[i])

    for i in range(0, len(coord_array)-1, 2):
        for j in range(0, 2):
            coord_one = coord_array[i]
            coord_two = coord_array[i+1]
            if coord_one[j] == coord_two[j]:
                if j == 0 :
                    for k in range(min(coord_one[1], coord_two[1]), max(coord_one[1], coord_two[1])+1):
                        grid[coord_one[j]][k] += 1
                else:
                    for k in range(min(coord_one[0], coord_two[0]), max(coord_one[0], coord_two[0])+1):
                        grid[k][coord_one[j]] += 1

    total_count = 0
    for row in grid:
        for square in row:
            if square >= 2:
                total_count += 1
                
    return total_count

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []
    coord_array = []
    grid = [[0 for i in range(1000)] for j in range(1000)]

    for line in input:
        input_array.append(line.strip().split(' -> '))

    for i in range(len(input_array)):
        for j in range(len(input_array[i])):
            coord_array.append(input_array[i][j].split(','))

    for row in coord_array:
        for i in range(len(row)):
            row[i] = int(row[i])

    for i in range(0, len(coord_array)-1, 2):
        for j in range(0, 2):
            coord_one = coord_array[i]
            coord_two = coord_array[i+1]

            x_diff = coord_one[0] - coord_two[0]
            y_diff = coord_one[1] - coord_two[1]
            diagonal_present = abs(x_diff) == abs(y_diff)

            if coord_one[j] == coord_two[j]:
                if j == 0 :
                    for k in range(min(coord_one[1], coord_two[1]), max(coord_one[1], coord_two[1])+1):
                        grid[coord_one[j]][k] += 1
                else:
                    for k in range(min(coord_one[0], coord_two[0]), max(coord_one[0], coord_two[0])+1):
                        grid[k][coord_one[j]] += 1
            elif diagonal_present and j != 1:
                for m in range(0, abs(x_diff)+1):
                    for n in range(m, abs(y_diff)+1):
                        if coord_one[0] > coord_two[0]:
                            current_coord, other_coord = coord_one, coord_two
                        else:
                            current_coord, other_coord = coord_two, coord_one

                        if current_coord[1] - other_coord[1] > 0:
                            grid[current_coord[0] - m][current_coord[1] - n] += 1
                        else:
                            grid[current_coord[0] - m][current_coord[1] + n] += 1
                        break

    total_count = 0
    for row in grid:
        for square in row:
            if square >= 2:
                total_count += 1
                
    return total_count
def prob1(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(list(line.strip()))

    risk_sum = 0
    for i in range(len(input_array)):
        for j in range(len(input_array[i])):
            current = int(input_array[i][j])

            top = int(input_array[i-1][j]) if i > 0 else 99
            down = int(input_array[i+1][j]) if i < len(input_array) - 1 else 99
            right = int(input_array[i][j+1]) if j < len(input_array[0]) - 1 else 99
            left = int(input_array[i][j-1]) if j > 0 else 99 

            if current < min(top, down, right, left):
                risk_sum += current + 1

    return risk_sum

def basin_search(input, row, column, starting):
    # Recursion through the four adjacent points and adds it to the basin unless it is a 9, or is out of bounds
    # until no new points can be added (all surrounding points are 9's, or out of bounds)
    # Returns the size of the basin
    checks = [(1,0), (-1,0), (0,1), (0,-1)]
    for check in checks:
        new_row = row + check[0]
        new_col = column + check[1]

        if new_row >= 0 and new_row < len(input) and new_col >= 0 and new_col < len(input[0]):
            if input[new_row][new_col] != '9':
                if (new_row, new_col) not in starting:
                    starting.append((new_row, new_col))
                    basin_search(input, new_row, new_col, starting)
    
    return len(starting)
    
def prob2(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(list(line.strip()))

    basin_sizes = []
    for i in range(len(input_array)):
        for j in range(len(input_array[i])):
            current = int(input_array[i][j])

            top = int(input_array[i-1][j]) if i > 0 else 99
            down = int(input_array[i+1][j]) if i < len(input_array) - 1 else 99
            right = int(input_array[i][j+1]) if j < len(input_array[0]) - 1 else 99
            left = int(input_array[i][j-1]) if j > 0 else 99 

            if current < min(top, down, right, left):
                basin_sizes.append(basin_search(input_array, i, j, [(i, j)]))

    sorted_basins = sorted(basin_sizes, reverse=True)
    
    return sorted_basins[0] * sorted_basins[1] * sorted_basins[2]
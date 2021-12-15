def prob1(file):
    input = open(file, "r").read().split('\n\n')

    coordinates = [list(map(int, y)) for y in [x.split(',') for x in input[0].split('\n')]]
    folds = [(z[0],int(z[1])) for z in [y.split('=') for y in [input[1].split()[x] for x in range(2, len(input[1].split()), 3)]]]

    max_x = max_y = 0
    for coord in coordinates:
        max_y = coord[0] if coord[0] > max_y else max_y
        max_x = coord[1] if coord[1] > max_x else max_x

    y_dim = folds[0][1] if folds[0][0] == 'y' else max_y + 1
    x_dim = folds[0][1] if folds[0][0] == 'x' else max_x + 1

    grid = [[0 for _ in range(x_dim)] for _ in range(y_dim)]

    for coord in coordinates:
        x,y = coord
        fold = folds[0]
        x = fold[1] - abs(x - fold[1]) if fold[0] == 'x' else x
        y = fold[1] - abs(y - fold[1]) if fold[0] == 'y' else y
        if x < 0 or y < 0:
            continue
        grid[y][x] = 1

    return sum(sum(y) for y in grid)

def prob2(file):
    input = open(file, "r").read().split('\n\n')

    coordinates = [list(map(int, y)) for y in [x.split(',') for x in input[0].split('\n')]]
    folds = [(z[0],int(z[1])) for z in [y.split('=') for y in [input[1].split()[x] for x in range(2, len(input[1].split()), 3)]]]

    max_x = max_y = 0
    for coord in coordinates:
        max_y = coord[0] if coord[0] > max_y else max_y
        max_x = coord[1] if coord[1] > max_x else max_x

    min_y_fold = min_x_fold = -1
    for fold in folds:
        axis, coord = fold[0], fold[1]
        if axis == 'y':
            min_y_fold = coord if min_y_fold < 0 else min(min_y_fold, coord)
        elif axis == 'x':
            min_x_fold = coord if min_x_fold < 0 else min(min_x_fold, coord)

    y_dim = min_y_fold if min_y_fold > 0 else max_y + 1
    x_dim = min_x_fold if min_x_fold > 0 else max_x + 1

    grid = [[0 for _ in range(x_dim)] for _ in range(y_dim)]

    for coord in coordinates:
        x,y = coord
        for fold in folds:
            x = fold[1] - abs(x - fold[1]) if fold[0] == 'x' else x
            y = fold[1] - abs(y - fold[1]) if fold[0] == 'y' else y
        if x < 0 or y < 0:
            continue
        grid[y][x] = 1

    output = []
    for y in grid:
        for x in y:
            output.append("#") if x else output.append(' ')
        output.append("\n")

    return "".join(output)
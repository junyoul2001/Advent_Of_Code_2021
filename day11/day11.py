def flash(i, j, grid, flashed):
    flashed.append((i,j))

    for ni,nj in [(i-1,j),(i-1,j+1),(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1),(i-1,j-1)]:
        if (ni >= 0 and ni < len(grid)) and (nj >= 0 and nj < len(grid[0])):
            grid[ni][nj] += 1
            if grid[ni][nj] > 9 and (ni, nj) not in flashed:
                flash(ni, nj, grid, flashed)

    return flashed

def prob1(file):
    input = open(file, "r").readlines()
    input_array = []
    steps = 100

    for line in input:
        input_array.append(list(line.strip()))

    octopuses = [[int(y) for y in x] for x in input_array]

    flashes = 0
    for _ in range(steps):
        flashed = []
        for i in range(len(octopuses)):
            for j in range(len(octopuses[i])):
                octopuses[i][j] += 1
                if octopuses[i][j] > 9:
                    flashed = flash(i, j, octopuses, flashed)
                for coord in flashed:
                    octopuses[coord[0]][coord[1]] = 0
        flashes += len(flashed)

    return flashes

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(list(line.strip()))

    octopuses = [[int(y) for y in x] for x in input_array]

    steps = 0
    all_flash = False
    while not all_flash:
        for i in range(len(octopuses)):
            for j in range(len(octopuses[i])):
                octopuses[i][j] += 1
                if octopuses[i][j] > 9:
                    flashed = flash(i, j, octopuses, [])
                for coord in flashed:
                    octopuses[coord[0]][coord[1]] = 0

        if len(flashed) == len(octopuses) * len(octopuses[i]):
            all_flash = True
            
        steps += 1

    return steps

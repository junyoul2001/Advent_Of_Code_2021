lines = open("input.txt", "r").readlines()

coordinates = []
folds = []
for line in lines:
    if not line.strip():
        continue
    if line.startswith("fold along"):
        fold_axis, fold_coord = line.split()[2].split("=")
        folds.append((fold_axis, int(fold_coord)))
    else:
        x, y = line.split(",")
        coordinates.append((int(x), int(y)))

X = max(x for x, _ in coordinates)
Y = max(y for _, y in coordinates)
sheet = [[False for _ in range(Y + 1)] for __ in range(X + 1)]
for x, y in coordinates:
    sheet[x][y] = True


def fold_x(sh, fold_coord):
    new_sh = [[False for _ in range(len(sh[0]))] for __ in range(fold_coord)]
    for y in range(len(sh[0])):
        for x in range(fold_coord):
            new_sh[x][y] = sh[x][y]
            if len(sh) - 2 * fold_coord - 1 <= x:
                new_sh[x][y] = sh[x][y] or sh[2 * fold_coord - x][y]
    return new_sh


def fold_y(sh, fold_coord):
    new_sh = [[False for _ in range(fold_coord)] for __ in range(len(sh))]
    for x in range(len(sh)):
        for y in range(fold_coord):
            new_sh[x][y] = sh[x][y]
            if len(sh[0]) - 2 * fold_coord - 1 <= y:
                new_sh[x][y] = sh[x][y] or sh[x][2 * fold_coord - y]
    return new_sh


def fold_sheet(sh, fold_axis, fold_coord):
    assert fold_axis in ["x", "y"]
    if fold_axis == "x":
        return fold_x(sh, fold_coord)
    return fold_y(sh, fold_coord)


print("Part 1:", sum(1 for row in fold_sheet(sheet, *folds[0]) for pixel in row if pixel))


for fold in folds:
    sheet = fold_sheet(sheet, *fold)
print("Part 2:")
for row in zip(*sheet):
    print("".join("#" if c else "." for c in row))
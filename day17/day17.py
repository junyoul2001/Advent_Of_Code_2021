def prob1(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.strip().split(': ')[1].split(', '))

    y_range = list(map(int, input_array[0][1].split('=')[1].split('..')))

    y_pos = 0
    y_vel = (min(y_range) * -1) - 1
    while y_vel:
        y_pos += y_vel
        y_vel -= 1

    return y_pos

def check_in_target(x_vel, y_vel, x_range, y_range):
    x = y = 0
    while True:
        x += x_vel
        y += y_vel

        x_vel = x_vel - 1 if x_vel > 0 else x_vel + 1 if x_vel < 0 else 0
        y_vel -= 1

        if (min(x_range) <= x <= max(x_range)) and (min(y_range) <= y <= max(y_range)):
            return True

        if x > max(x_range) or y < min(y_range):
            return False

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.strip().split(': ')[1].split(', '))

    x_range = list(map(int, input_array[0][0].split('=')[1].split('..')))
    y_range = list(map(int, input_array[0][1].split('=')[1].split('..')))

    total_vel = 0
    for x_vel in range(0, max(x_range) + 1):
        for y_vel in range(min(y_range), (-1 * min(y_range))):
            if check_in_target(x_vel, y_vel, x_range, y_range):
                total_vel += 1

    return total_vel
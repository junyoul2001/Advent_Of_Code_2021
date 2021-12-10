def board_win(board: list):
    # Returns True if there is a row or column of '-1'
    for row in board:
        if row.count('-1') == len(row):
            return True

    for i in range(len(board[0])):
        col_count = 0
        for j in range(len(board)):
            if board[j][i] == '-1':
                col_count += 1
                if col_count == len(board):
                    return True
                    
    return False

def board_sum(board: list):
    # Returns the sum of all numbers in a board that is not '-1'
    sum = 0
    for row in board:
        for numbers in row:
            if int(numbers) > 0:
                sum += int(numbers)
    return sum

def prob1(file):
    input = open(file, "r").read().split('\n\n')

    bingo_numbers = input[0].split(',')
    boards = input[1:]

    split_boards = [[x.split() for x in board.split('\n')] for board in boards]

    # looping through each bingo board to find any matches
    win_board = None
    win_number = None
    win_flag = False
    for bingo_number in bingo_numbers:
        for board in split_boards:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == bingo_number:
                        board[i][j] = '-1'
            if board_win(board):
                win_flag = True
                win_board = board
                win_number = bingo_number
        if win_flag:
            break

    return board_sum(win_board) * int(win_number)

def prob2(file):
    input = open(file, "r").read().split('\n\n')

    bingo_numbers = input[0].split(',')
    boards = input[1:]

    split_boards = [[x.split() for x in board.split('\n')] for board in boards]

    # looping through each bingo board to find any matches
    win_count = 0
    last_win_board = None
    last_win_number = None
    last_win_flag = False
    for bingo_number in bingo_numbers:
        for i in range(len(split_boards)):
            for j in range(len(split_boards[i])):
                for k in range(len(split_boards[i][j])):
                    if split_boards[i][j][k] == bingo_number:
                        split_boards[i][j][k] = '-1'
            if split_boards[i] != []:
                if board_win(split_boards[i]):
                    win_count += 1
                    current_board = split_boards[i]
                    split_boards[i] = []
                    if win_count == len(split_boards):
                        last_win_board = current_board
                        last_win_number = bingo_number
                        last_win_flag = True
        if last_win_flag:
            break
    
    return board_sum(last_win_board) * int(last_win_number)
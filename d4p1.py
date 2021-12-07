from puzzleinput import lines

draw_order = [int(x) for x in lines[0].split(',')]
boards = []
board = []
called = []
for line in lines[2:]:
    if not line.strip():
        boards.append(board)
        board = []
        continue
    row = line.replace("  ", " ")
    row = [int(x) for x in row.split(' ')]
    board.append(row)
boards.append(board)


def calculate_score(board):
    unmarked_sum = 0
    for row in board:
        for number in row:
            if number not in called:
                unmarked_sum += number
    return unmarked_sum * called[-1]


def check_board_victorious(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] not in called:
                break
        else:
            return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[j][i] not in called:
                break
        else:
            return True
    return False


victorious_boards = []
to_remove = []
for number in draw_order:
    for b in to_remove:
        boards.remove(b)
    to_remove = []
    called.append(number)

    for board in boards:
        if check_board_victorious(board):
            to_remove.append(board)
            if len(boards) == 1:
                print(calculate_score(boards[0]))
                exit()

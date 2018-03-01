"""
Tic-Tac-Toe console game for two Players
"""


def print_board(board_grid):
    print("-------------------")
    for i in range(3):
        # Inner
        print("|", end='')
        for j in range(3):
            if board_grid[i][j] is None:
                print("     ", end='')
            else:
                print("  {0}  ".format(board_grid[i][j]), end='')
            print("|", end='')
        print()

        print("-------------------")


def check_win(board_grid, pos_x, pos_y):
    mark = board_grid[pos_x][pos_y]

    # Check horizontally
    win = True
    for i in range(3):
        if board_grid[i][pos_y] != mark:
            win = False
            break

    if win is True:
        return win

    # Check vertically
    win = True
    for i in range(3):
        if board_grid[pos_x][i] != mark:
            win = False
            break

    if win is True:
        return win

    if (pos_x == 1 and pos_y == 1) \
            or ((pos_x == 0) and (pos_y == 0)) \
            or ((pos_x == 2) and (pos_y == 2)):
        # Check from Up-left to Bottom-right
        win = True
        for i in range(3):
                if board_grid[i][i] != mark:
                    win = False
                    break

    if win is True:
        return win

    if (pos_x == 1 and pos_y == 1) \
            or ((pos_x == 0) and (pos_y == 2)) \
            or ((pos_x == 2) and (pos_y == 0)):
        # Check from Up-right to Bottom-left
        win = True
        for i, j in zip(range(3), reversed(range(3))):
                if board_grid[i][j] != mark:
                    win = False
                    break

    return win


def check_full(board_grid):
    ret = True
    for i in range(3):
        for j in range(3):
            if board_grid[i][j] is None:
                ret = False
    return ret


def tictactoe_fortwo():
    print("Tic-Tac-Toe Game\n" + "Input X to stop\n")

    markers = ['X', 'O']

    # board_grid = [['' for i in range(3)] for i in range(3)]
    board_grid = [[None for i in range(3)] for i in range(3)]

    print_board(board_grid)

    idx_mark = 0
    while True:
        cur_mark = markers[idx_mark]

        in_str = input("Put {0}. Select 1~9 : ".format(cur_mark))

        if in_str.upper() == 'X':
            break
        elif not in_str.isdecimal():
            print("Please intput number")
            continue

        in_num = int(in_str) - 1
        if not (0 <= in_num <= 8):
            print("Please intput 1~9")
            continue
        elif board_grid[in_num // 3][in_num % 3] is not None:
            print("Not empty. Try again.")
            continue

        board_grid[in_num // 3][in_num % 3] = cur_mark

        print()

        print_board(board_grid)

        if check_win(board_grid, in_num // 3, in_num % 3) is True:
            print("Game Over : {0} Won!".format(cur_mark))
            break
        elif check_full(board_grid) is True:
            print("Game Over : Draw!")
            break

        idx_mark = (idx_mark + 1) % 2


if __name__ == '__main__':
    tictactoe_fortwo()


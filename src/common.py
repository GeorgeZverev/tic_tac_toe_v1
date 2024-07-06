import os


def draw_board(board: []):
    # os.system('cls')
    for horz in board:
        row = ""
        for square in horz:
            row += square + '  '
        print(row)


def map_from_coordinates(coordinate: str) -> (int, int):
    # 3          .
    # 2      .
    # 1  .
    #    a   b   c
    if 'a' in coordinate:
        y = 0
    elif 'b' in coordinate:
        y = 1
    elif 'c' in coordinate:
        y = 2
    else:
        y = -1
    if '1' in coordinate:
        x = 2
    elif '2' in coordinate:
        x = 1
    elif '3' in coordinate:
        x = 0
    else:
        x = -1
    return x, y

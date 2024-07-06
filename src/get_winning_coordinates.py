

def build_diagonal(board: [], coord: [], col_index: int, index: int, op: str) -> int:
    coord.append(board[col_index][index])
    if op == "+":
        index += 1
    else:
        index -= 1
    return index

def get_winning_coordinates(board: []) -> []:
    all_coordinates_list = []
    dgnl_a_coord = []
    dgnl_b_coord = []
    dgnl_a_index = 0
    dgnl_b_index = len(board[0]) - 1
    for col_index, _ in enumerate(board):
        row_coord = []
        col_coord = []
        for row_index, _ in enumerate(board):
            row_coord.append(board[col_index][row_index])
        dgnl_a_index = build_diagonal(board, dgnl_a_coord, col_index, dgnl_a_index, "+")
        dgnl_b_index = build_diagonal(board, dgnl_b_coord, col_index, dgnl_b_index, "-")
        for row_index, _ in enumerate(board):
            col_coord.append(board[row_index][col_index])
        all_coordinates_list.append(row_coord)
        all_coordinates_list.append(col_coord)
    dgnl_b_coord.reverse()
    all_coordinates_list.append(dgnl_a_coord)
    all_coordinates_list.append(dgnl_b_coord)
    return all_coordinates_list

if __name__ == '__main__':
    board = [['a1','b1','c1'],['a2','b2','c2'],['a3','b3','c3']]
    all_coordinates = get_winning_coordinates(board)
    print(all_coordinates)
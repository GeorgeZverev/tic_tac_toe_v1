import os
from my_error import MyError
from common import *
from play_for_computer_v4 import *

board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
valid_coordinates = [["a3", "b3", "c3"], ["a2", "b2", "c2"], ["a1", "b1", "c1"]]


def accept_coordinate() -> (str, str):
    coordinate = input("Enter a coordinate: ")
    if coordinate.isupper():
        coordinate = coordinate.lower()
        token = 'o'
    else:
        token = 'x'
    return (coordinate, token)


def accept_mode() -> str:
    mode = input("Select who starts the game(h or c): ")
    return mode


def is_valid(coordinate: str, list_coordinate: []) -> bool:
    for coordinates in list_coordinate:
        if coordinate in coordinates:
            return True
    return False


def check_winner(board_param: []) -> int:
    right_coordinates = get_winning_coordinates(board_param)
    for triple in right_coordinates:
        if triple[0] != '.' and triple.count(triple[0]) == len(triple):
            if triple[0] == 'x':
                return 1
            else:
                return 2
    if not is_free_square_present(board_param):
        return 3
    return 0


def print_current_state(board_param: [], coord_names: []) -> {}:
    coordinates = {}
    for row_index, row in enumerate(board_param):
        for col_index, _ in enumerate(row):
            coordinates[coord_names[len(board_param) - 1 - row_index][col_index]] = \
                board_param[len(board_param) - 1 - row_index][col_index]
    return coordinates


def update_board(board: [], coordinate: str, token: str) -> bool:
    x, y = map_from_coordinates(coordinate)
    if board[x][y] == '.':
        board[x][y] = token
        return True
    return False


def play_round_for_human(board: []) -> (str, str):
    coordinate, token = accept_coordinate()
    play_human_round(board, coordinate, token)
    return coordinate, token


def play_human_round(board: [], coordinate: str, token: str) -> bool:
    success = update_board(board, coordinate, token)
    draw_board(board)
    return success


def print_current_coordinates(current_coord: {}):
    coordinates_to_print = ["board: "]
    for key, value in current_coord.items():
        if value != '.':
            coordinates_to_print.append(key + "(" + value + ")")
            coordinates_to_print.append(", ")
    coordinates_to_print[-1] = "."
    # print(''.join(coordinates_to_print))


def update_last_coordinate(board: [], token: str):
    if token == 'x':
        machine_token = 'o'
    else:
        machine_token = 'x'
    for x, array in enumerate(board):
        for y, element in enumerate(array):
            if element == '.':
                board[x][y] = machine_token
    draw_board(board)


def define_turn() -> int:
    mode = accept_mode()
    if mode != 'h' and mode != 'c':
        print('You chose a non-existent mode')
        exit(1)
    if mode == 'h':
        return 0
    else:
        return 1


def generate_coordinate() -> (str, str):
    if turn % 2 == 0:
        return play_round_for_human(board)
    else:
        try:
            return play_round_for_computer(board, True, valid_coordinates)
        except MyError:
            raise MyError


def check_for_game_over(coordinate_param: str) -> int:
    if is_valid(coordinate_param, valid_coordinates):
        current_coordinates = print_current_state(board, valid_coordinates)
        print_current_coordinates(current_coordinates)
        return check_winner(board)
    return -1

if __name__ == '__main__':
    attempts = 0
    turn = define_turn()
    while True:
        try:
            (coordinate, token) = generate_coordinate()
        except MyError:
            update_last_coordinate(board, token)
            print("\nDraw")
            break
        turn += 1
        result = check_for_game_over(coordinate)
        if result >= 0:
            if result == 1:
                print("\n'X's won")
                break
            elif result == 2:
                print("\n'O's won")
                break
            elif result == 3:
                print("\nDraw")
                break
        elif attempts < 2:
            attempts += 1
            continue
        else:
            print("Game over")
            break

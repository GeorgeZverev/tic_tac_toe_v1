import random

from common import *

from get_winning_coordinates import get_winning_coordinates

def play_round_for_computer(board: [], flag: bool, valid_coordinates: []) -> str:
    if flag == True:
        token = 'x'
    else:
        token = 'o'
    coordinate = play_computer_round(board, token, valid_coordinates)
    return coordinate

def play_computer_round(board: [], token: str, valid_coordinates: []):
    # compute_coordinate(board, token)
    coordinate = compute_better_coordinate(board, token, valid_coordinates)
    print('----------')
    draw_board(board)
    return coordinate

def compute_better_coordinate(board: [], token: str, valid_coordinates: []):
    counter = 0
    while True:
        x = random.randrange(3)
        y = random.randrange(3)
        proposed_coordinate = map_to_coordinates(x, y)
        print('proposed_coordinate:',proposed_coordinate)
        counter += 1
        if counter == 30:
            break
        combined_list = create_combined_list(board, valid_coordinates)
        winning_coordinate = is_computer_win_in_one_move(combined_list, token)
        if winning_coordinate is not None:
            (x, y) = map_from_coordinates(winning_coordinate)
            not_bad_coord_flag = True
        else:
            winning_coordinate = is_human_win_in_one_move(combined_list, token)
        if winning_coordinate is not None:
            (x, y) = map_from_coordinates(winning_coordinate)
            not_bad_coord_flag = True
            # winning_coordinate = is_win_in_one_move(combined_list, token)
            # if winning_coordinate is not None:
            #     (x, y) = map_from_coordinates(winning_coordinate)
            #     print('winning_coordinate:', winning_coordinate)
            #     not_bad_coord_flag = True
        else:
            not_bad_coord_flag = is_not_bad_coord(board, valid_coordinates, proposed_coordinate, token)
        if board[x][y] == '.' and not_bad_coord_flag:
            if token == 'x':
                board[x][y] = 'o'
                return proposed_coordinate
            else:
                board[x][y] = 'x'
                return proposed_coordinate
            break


def map_to_coordinates(x: int, y: int) -> str:
    # 3          .
    # 2      .
    # 1  .
    #    a   b   c
    coord_1 = ''
    coord_2 = ''
    if y == 0:
        coord_1 = 'a'
    elif y == 1:
        coord_1 = 'b'
    else:
        coord_1 = 'c'
    if x == 2:
        coord_2 = '1'
    elif x == 1:
        coord_2 = '2'
    else:
        coord_2 = '3'
    return coord_1 + coord_2


# def map_from_coordinates(coordinate: str) -> (int, int):
#     # 3          .
#     # 2      .
#     # 1  .
#     #    a   b   c
#     if 'a' in coordinate:
#         y = 0
#     elif 'b' in coordinate:
#         y = 1
#     else:
#         y = 2
#     if '1' in coordinate:
#         x = 2
#     elif '2' in coordinate:
#         x = 1
#     else:
#         x = 0
#     return (x, y)


# def draw_board_for_computer(board: []):
#     #os.system('cls')
#     for horz in board:
#         row = ""
#         for square in horz:
#             row += square + '  '
#         print(row)


def create_combined_list(board: [], valid_coordinates: []) -> []:
    all_coordinates_list = get_winning_coordinates(board)
    #print(all_coordinates_list)
    current_state_list = get_winning_coordinates(valid_coordinates)
    #print(current_state_list)
    combined_list = select_lists(all_coordinates_list, current_state_list)
    return combined_list


def is_computer_win_in_one_move(combined_list: [], token: str) -> str | None:
    winning_square = ''
    for list in combined_list:
        counter_tokens = 0
        counter_free = 0
        if token == 'x':
            computer_token = 'o'
        else:
            computer_token = 'x'
        for element in list:
            if computer_token in element:
                counter_tokens += 1
            elif '.' in element:
                counter_free += 1
                winning_square = element
        if counter_tokens == len(list)-1 and counter_free > 0:
            return winning_square
    return None


def is_human_win_in_one_move(combined_list: [], token: str) -> str | None:
    winning_square = ''
    for list in combined_list:
        counter_tokens = 0
        counter_free = 0
        for element in list:
            if token in element:
                counter_tokens += 1
            elif '.' in element:
                counter_free += 1
                winning_square = element
        if counter_tokens == len(list)-1 and counter_free > 0:
            return winning_square
    return None


def is_not_bad_coord(board: [], valid_coordinates: [], proposed_coordinate: str, token: str) -> bool:
    combined_list = create_combined_list(board, valid_coordinates)
    if is_free_of_enemys_token(combined_list, token, proposed_coordinate):
        return True
    return False


def select_lists(all_coordinates_list: [], current_state_list: []) -> []:
    combined_list = []
    for x, coordinates_list in enumerate(all_coordinates_list):
        elements = []
        for y, coordinates in enumerate(coordinates_list):
            coordinate_x = coordinates_list[y]
            coordinate_y = current_state_list[x][y]
            element = coordinate_y + coordinate_x
            elements.append(element)
        combined_list.append(elements)
    #print("combined_list: ", combined_list)
    return combined_list

def is_free_of_enemys_token(combined_list: [], token: str, proposed_coordinate: str) -> bool:
    selected_list = select_lists_with_possible_coordinates(combined_list, token)
    proposed_coordinate = proposed_coordinate + '.'
    for outer_list in selected_list:
        if proposed_coordinate in outer_list:
            return True
    return False

def select_lists_with_possible_coordinates(selected_list: [], token: str) -> []:
    array = []
    for list in selected_list:
        bad_token_flag = False
        for element in list:
            if token in element:
                bad_token_flag = True
        if bad_token_flag == False:
            array.append(list)
            break
    return array

def is_free_square_present(board: []) -> bool:
    for x, list in enumerate(board):
        for y, element in enumerate(list):
            if board[x][y] == '.':
                return True
    return False
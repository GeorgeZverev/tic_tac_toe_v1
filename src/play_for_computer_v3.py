import random
from collections import Counter
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
        print('proposed_coordinate:', proposed_coordinate)
        counter += 1
        if counter == 100:
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
        else:
            proposed_coordinate = propose_best_coordinate_v2(proposed_coordinate, combined_list, token, board, x, y, valid_coordinates)
            (x, y) = map_from_coordinates(proposed_coordinate)
            not_bad_coord_flag = is_not_bad_coord(board, valid_coordinates, proposed_coordinate, token)
        if board[x][y] == '.' and not_bad_coord_flag:
            if token == 'x':
                board[x][y] = 'o'
                return proposed_coordinate
            else:
                board[x][y] = 'x'
                return proposed_coordinate
            break


def flat_l(selected_lists: [], j: int ) -> []:
    flat_list = []
    for list in selected_lists:
        for element in list:
            if j == 1:
                if element[-1] == '.':
                    flat_list.append(element)
            else:
                flat_list.append(element)
    return  flat_list


def copy_board_with_potential_coordinates(board: [], coordinates:[], machine_token: str, token: str, valid_coordinates: []) -> []:
    if token == 'o':
        token = 'x'
    else:
        token = 'o'
    array_potential_copy_coordinates = {}
    for element in coordinates:
        copy_board =[e.copy() for e in board]
        x, y = map_from_coordinates(element)
        copy_board[x][y] = machine_token
        combined_list = create_combined_list(copy_board, valid_coordinates)
        select_list = select_lists_with_possible_coordinates(combined_list, token)
        array_potential_copy_coordinates[element] = select_list
        # array_potential_copy_coordinates.append(select_list)
    return array_potential_copy_coordinates


def find_lists_with_max_token(array_potential_coordinates: {}) -> []:
    j = 2
    for key, value in array_potential_coordinates.items():
        counter = 0
        two_d_lists = value
        flat_td_list = flat_l(two_d_lists, j)
        for element in flat_td_list:
            if element[2] != '.':
                counter += 1
        array_potential_coordinates[key] = counter
    print(array_potential_coordinates)
    max_key = max(array_potential_coordinates.values())
    array_max_token = [k for k,v in array_potential_coordinates.items() if v == max_key]
    return array_max_token


def propose_best_coordinate(coordinate: str, combined_list: [], token: str, board: [], x: int, y: int) -> {}:  # free coord max times and free, selected list , 3 - 3
    selected_lists = select_lists_with_possible_coordinates(combined_list, token)
    j = 1
    flat_list = flat_l(selected_lists, j)
    countered_dict = dict(Counter(flat_list))
    print(countered_dict)
    # max_key = max(countered_dict, key=countered_dict.get)
    max_key = max(countered_dict.values())
    dict_max_keys = [k for k,v in countered_dict.items() if v == max_key]
    #coordinate = max_key.replace('.', '')
    dict_max_keys = [element[:-1] for element in dict_max_keys]
    return dict_max_keys


def propose_best_coordinate_v2(coordinate: str, combined_list: [], token: str, board: [], x: int, y: int, valid_coordinates: []) -> str:
    if token == 'x':
        token = 'o'
        machine_token = 'o'
    else:
        token = 'x'
        machine_token = 'x'
    # 1.  List me all arrays where OPPONENT can move &  2. Select coordinates with max occurences
    coordinates = propose_best_coordinate(coordinate, combined_list, token, board, x, y)
    print(coordinates)
    # 1. List me all arrays where OPPONENT can move
    # selected_lists = select_lists_with_possible_coordinates(combined_list, token)
    # 2. Select coordinates with max occurences
    # flat_list = flat_l(selected_lists)
    # countered_dict = Counter(flat_list)
    # max_key = max(countered_dict, key=countered_dict.get)
    # coordinate = max_key.replace('.', '')
    # ll = []
    # ll.append(coordinate)
    # 3. List me all arrays where WE can move
    array_potential_coordinates = copy_board_with_potential_coordinates(board, coordinates, machine_token, token, valid_coordinates)
    # 4. Select list with max of our tokens
    max_token_coordinates = find_lists_with_max_token(array_potential_coordinates)
    # 5. Select single coordinate
    result = max_token_coordinates[0]
    return result


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
            # break
    return array


def is_free_square_present(board: []) -> bool:
    for x, list in enumerate(board):
        for y, element in enumerate(list):
            if board[x][y] == '.':
                return True
    return False
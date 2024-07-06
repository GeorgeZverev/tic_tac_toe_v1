import random

from get_winning_coordinates import get_winning_coordinates


def accept_coordinate() -> (str, str):
    coordinate = input("Enter coordinate: ")
    if coordinate.isupper():
        coordinate = coordinate.lower()
        token = 'o'
    else:
        token = 'x'
    return (coordinate, token)

def is_valid(coordinate: str, list_coordinate: []) -> bool:
    for coordinates in list_coordinate:
        if coordinate in coordinates:
            return True
    return False

def compute_coordinate(board: str, token: str):
    while True:
        x = random.randrange(3)
        y = random.randrange(3)
        if board[x][y] == '.':
            if token == 'x':
                board[x][y] = 'o'
            else:
                board[x][y] = 'x'
            break


def select_lists_with_possible_coordinates(selected_list: [], token:str) -> []:
    array = []
    for list in selected_list:
        bad_token_flag = False
        for element in list:
            if token in element:
                bad_token_flag = True
        if bad_token_flag == False:
            array.append(list)
            print(array)
            break
    return array



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
    # print("combined_list: ", combined_list)
    return combined_list



def is_not_bad_coord(board: [], valid_coordinates: [], proposed_coordinate: str, token: str) -> bool:
    all_coordinates_list = get_winning_coordinates(board)
    #print(all_coordinates_list)
    current_state_list = get_winning_coordinates(valid_coordinates)
    #print(current_state_list)
    combined_list = select_lists(all_coordinates_list, current_state_list)
    selected_list = select_lists_with_possible_coordinates(combined_list, token)
    if len(selected_list) == 0:
        return False
    proposed_coordinate = proposed_coordinate + '.'
    for outer_list in selected_list:
        if proposed_coordinate in outer_list:
            return True
    return False



def compute_better_coordinate(board: [], token: str, valid_coordinates: []):
    while True:
        x = random.randrange(3)
        y = random.randrange(3)
        proposed_coordinate = map_to_coordinates(x, y)
        isntbad = is_not_bad_coord(board, valid_coordinates, proposed_coordinate, token)
        if board[x][y] == '.' and isntbad:
            if token == 'x':
                board[x][y] = 'o'
            elif token == 'o':
                board[x][y] = 'x'
            break
            if isntbad == False:
                break





def draw_board(board: []):
    for horz in board:
        row = ""
        for square in horz:
            row += square + '  '
        print(row)


def check_winner(board: []) -> int:
    right_coordinates = get_winning_coordinates(board)
    for triple in right_coordinates:
        if triple[0] != '.' and triple.count(triple[0]) == len(triple):
            if triple[0] == 'x':
                return 1
            else:
                return 2
    return 0


def print_current_state(board: [], coord_names: []) -> {}:
    coordinates = {}
    for row_index, row in enumerate(board):
        for col_index, _ in enumerate(row):
                coordinates[coord_names[len(board)-1-row_index][col_index]] = board[len(board)-1-row_index][col_index]
    #print(coordinates)
                #print('Board:', coord_names[len(coord_names)-1-row_index][col_index], "(", board[len(board)-1-row_index][col_index] ,")")
    return coordinates


def update_board(board: [], coordinate: str, token: str) -> bool:
    x, y = map_from_coordinates(coordinate)
    if board[x][y] == '.':
        board[x][y] = token
        return True
    return False

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
    if x == 1:
        coord_2 = '1'
    elif x == 2:
        coord_2 = '2'
    else:
        coord_2 = '3'
    return coord_1 + coord_2



def map_from_coordinates(coordinate: str) -> (int, int):
    # 3          .
    # 2      .
    # 1  .
    #    a   b   c
    if 'a' in coordinate:
        y = 0
    elif 'b' in coordinate:
        y = 1
    else:
        y = 2
    if '1' in coordinate:
        x = 2
    elif '2' in coordinate:
        x = 1
    else:
        x = 0
    return (x, y)


def play_round(board: [], coordinate: str, token:str, valid_coordinates: []):
    success = play_human_round(board, coordinate, token)
    result = check_winner(board)
    if result != 0:
        success = False
    if success is True:
        play_computer_round(board, token, valid_coordinates)


def play_computer_round(board: [], token: str, valid_coordinates: []):
    # compute_coordinate(board, token)
    compute_better_coordinate(board, token, valid_coordinates)
    print('----------')
    draw_board(board)


def play_human_round(board: [], coordinate: str, token: str) -> bool:
    success = update_board(board, coordinate, token)
    draw_board(board)
    return success


def print_current_coordinates(current_coord: {}):
    coordinates_to_print = [ "board: " ]
    for key, value in current_coord.items():
        if value != '.':
            coordinates_to_print.append( key + "(" + value + ")")
            coordinates_to_print.append(", ")
    coordinates_to_print[-1] = "."
    print(''.join(coordinates_to_print))


# def print_current_coordinates(current_coord: {}):
#     coordinates_to_print = "board: "
#     counter_1 = 0
#     for key, value in current_coord.items():
#         if value != '.':
#             counter_1 += 1
#     counter_2 = 0
#     for key, value in current_coord.items():
#         if value != '.':
#             if counter_2 >= counter_1 - 1:
#                 coordinates_to_print += key + "(" + value + ")" + "."
#             else:
#                 coordinates_to_print += key + "(" + value + ")" + ", "
#             counter_2 += 1
#     print(coordinates_to_print)


if __name__ == '__main__':
    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    valid_coordinates = [["a3", "b3", "c3"],["a2", "b2", "c2"],["a1", "b1", "c1"]]
    attempts = 0
    while (True):
        (coordinate, token) = accept_coordinate()
        if is_valid(coordinate, valid_coordinates):
            play_round(board, coordinate, token, valid_coordinates)
            current_coordinates = print_current_state(board, valid_coordinates)
            print_current_coordinates(current_coordinates)
            # coordinates_to_print = "board: "
            # for key, value in current_coordinates.items():
            #     if value != '.':
            #         coordinates_to_print += key + "(" + value + ")" + "," + " "
            # print(coordinates_to_print)
            result = check_winner(board)
            if result == 1:
                print("\n'X's won")
                break
            elif result == 2:
                print("\n'O's won")
                break
        elif attempts < 2:
            attempts += 1
            continue
        else:
            print("Game over")
            break
        # else:
        #     while (True):
        #         coordinate = second_try()
        #         if is_valid(coordinate):
        #             counter += 1
        #             play_round(board, coordinate, 'x', counter)
        #             break

# def compute_coordinate(board: str, token: str):
#     while True:
#         x = random.randrange(3)
#         y = random.randrange(3)
#         if board[x][y] == '.':
#             if token == 'x':
#                 board[x][y] = 'o'
#             else:
#                 board[x][y] = 'x'
#             break


# def select_lists_with_possible_coordinates(selected_list: [], token: str) -> []:
#     array = []
#     for list in selected_list:
#         bad_token_flag = False
#         for element in list:
#             if token in element:
#                 bad_token_flag = True
#         if bad_token_flag == False:
#             array.append(list)
#             break
#     return array



# def is_win_in_one_move(combined_list: [], token: str) -> str | None: # is_human_win_in_one_move and is_computer_win_in_one_move
#     winning_square = ''
#     for list in combined_list:
#         counter_o = 0
#         counter_x = 0
#         counter_free = 0
#         for element in list:
#             if 'x' in element:
#                 counter_x += 1
#             elif 'o' in element:
#                 counter_o += 1
#             elif '.' in element:
#                 counter_free += 1
#                 winning_square = element
#         if (counter_o == len(list)-1 or counter_x == len(list)-1) and counter_free > 0:
#             return winning_square
#     return None


# def is_computer_win_in_one_move(combined_list: [], token: str) -> str | None:
#     winning_square = ''
#     for list in combined_list:
#         counter_tokens = 0
#         counter_free = 0
#         if token == 'x':
#             computer_token = 'o'
#         else:
#             computer_token = 'x'
#         for element in list:
#             if computer_token in element:
#                 counter_tokens += 1
#             elif '.' in element:
#                 counter_free += 1
#                 winning_square = element
#         if counter_tokens == len(list)-1 and counter_free > 0:
#             return winning_square
#     return None


# def is_human_win_in_one_move(combined_list: [], token: str) -> str | None:
#     winning_square = ''
#     for list in combined_list:
#         counter_tokens = 0
#         counter_free = 0
#         for element in list:
#             if token in element:
#                 counter_tokens += 1
#             elif '.' in element:
#                 counter_free += 1
#                 winning_square = element
#         if counter_tokens == len(list)-1 and counter_free > 0:
#             return winning_square
#     return None


# def select_lists(all_coordinates_list: [], current_state_list: []) -> []:
#     combined_list = []
#     for x, coordinates_list in enumerate(all_coordinates_list):
#         elements = []
#         for y, coordinates in enumerate(coordinates_list):
#             coordinate_x = coordinates_list[y]
#             coordinate_y = current_state_list[x][y]
#             element = coordinate_y + coordinate_x
#             elements.append(element)
#         combined_list.append(elements)
#     #print("combined_list: ", combined_list)
#     return combined_list


# def is_free_of_enemys_token(combined_list: [], token: str, proposed_coordinate: str) -> bool:
#     selected_list = select_lists_with_possible_coordinates(combined_list, token)
#     proposed_coordinate = proposed_coordinate + '.'
#     for outer_list in selected_list:
#         if proposed_coordinate in outer_list:
#             return True
#     return False
    # counter = 0
    # for element in outer_list:
    #     if element == proposed_coordinate:
    #         counter += 1




# def is_free_square_present(board: []) -> bool:
#     for x, list in enumerate(board):
#         for y, element in enumerate(list):
#             if board[x][y] == '.':
#                 return True
#     return False


# def create_combined_list(board: [], valid_coordinates: []) -> []:
#     all_coordinates_list = get_winning_coordinates(board)
#     #print(all_coordinates_list)
#     current_state_list = get_winning_coordinates(valid_coordinates)
#     #print(current_state_list)
#     combined_list = select_lists(all_coordinates_list, current_state_list)
#     return combined_list

# def is_not_bad_coord(board: [], valid_coordinates: [], proposed_coordinate: str, token: str) -> bool:
#     combined_list = create_combined_list(board, valid_coordinates)
#     if is_free_of_enemys_token(combined_list, token, proposed_coordinate):
#         return True
#     return False


# def compute_better_coordinate(board: [], token: str, valid_coordinates: []):
#     counter = 0
#     while True:
#         x = random.randrange(3)
#         y = random.randrange(3)
#         proposed_coordinate = map_to_coordinates(x, y)
#         print('proposed_coordinate:',proposed_coordinate)
#         counter += 1
#         if counter == 30:
#             break
#         combined_list = create_combined_list(board, valid_coordinates)
#         winning_coordinate = is_computer_win_in_one_move(combined_list, token)
#         if winning_coordinate is not None:
#             (x, y) = map_from_coordinates(winning_coordinate)
#             not_bad_coord_flag = True
#         else:
#             winning_coordinate = is_human_win_in_one_move(combined_list, token)
#         if winning_coordinate is not None:
#             (x, y) = map_from_coordinates(winning_coordinate)
#             not_bad_coord_flag = True
#             # winning_coordinate = is_win_in_one_move(combined_list, token)
#             # if winning_coordinate is not None:
#             #     (x, y) = map_from_coordinates(winning_coordinate)
#             #     print('winning_coordinate:', winning_coordinate)
#             #     not_bad_coord_flag = True
#         else:
#             not_bad_coord_flag = is_not_bad_coord(board, valid_coordinates, proposed_coordinate, token)
#         if board[x][y] == '.' and not_bad_coord_flag:
#             if token == 'x':
#                 board[x][y] = 'o'
#                 return proposed_coordinate
#             else:
#                 board[x][y] = 'x'
#                 return proposed_coordinate
#             break


# def draw_board(board: []):
#     #os.system('cls')
#     for horz in board:
#         row = ""
#         for square in horz:
#             row += square + '  '
#         print(row)

# def map_to_coordinates(x: int, y: int) -> str:
#     # 3          .
#     # 2      .
#     # 1  .
#     #    a   b   c
#     coord_1 = ''
#     coord_2 = ''
#     if y == 0:
#         coord_1 = 'a'
#     elif y == 1:
#         coord_1 = 'b'
#     else:
#         coord_1 = 'c'
#     if x == 2:
#         coord_2 = '1'
#     elif x == 1:
#         coord_2 = '2'
#     else:
#         coord_2 = '3'
#     return coord_1 + coord_2


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


# def play_round_for_computer(board: [], flag: bool, valid_coordinates: []) -> str:
#     if flag == True:
#         token = 'x'
#     else:
#         token = 'o'
#     coordinate = play_computer_round(board, token, valid_coordinates)
#     return coordinate


# def play_round_for_human(board: [], coordinate: str, token:str, valid_coordinates: []):
#     success = play_human_round(board, coordinate, token)
#     result = check_winner(board)
#     if result != 0:
#         success = False
#     if success is True:
#         play_computer_round(board, token, valid_coordinates)


# def play_computer_round(board: [], token: str, valid_coordinates: []):
#     # compute_coordinate(board, token)
#     coordinate = compute_better_coordinate(board, token, valid_coordinates)
#     print('----------')
#     draw_board(board)
#     return coordinate

# def print_current_coordinates(current_coord: {}):
#     coordinates_to_print = "board: "
#     counter_1 = 0
#     for key, value in current_coord.items():
#         if value != '.':
#             counter_1 += 1
#     counter_2 = 0
#     for key, value in current_coord.items():
#         if value != '.':
#             if counter_2 >= counter_1 - 1:
#                 coordinates_to_print += key + "(" + value + ")" + "."
#             else:
#                 coordinates_to_print += key + "(" + value + ")" + ", "
#             counter_2 += 1
#     print(coordinates_to_print)

            # coordinates_to_print = "board: "
            # for key, value in current_coordinates.items():
            #     if value != '.':
            #         coordinates_to_print += key + "(" + value + ")" + "," + " "
            # print(coordinates_to_print)

# if mode == 'h':
#     play_round_for_human(board, coordinate, token, valid_coordinates)
# else:
#     play_round_for_computer(board, coordinate, token, valid_coordinates)
# (coordinate, token) = accept_coordinate()

# play_round(board, coordinate, token, valid_coordinates)

    #print(coordinates)
                #print('Board:', coord_names[len(coord_names)-1-row_index][col_index], "(", board[len(board)-1-row_index][col_index] ,")")
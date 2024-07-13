import pytest
from main import *

board_1 = None


@pytest.fixture(autouse=True)
def foo():
    global board_1
    board_1 = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]


@pytest.fixture
def parameter_combined_list():
    pr_combined_list = create_combined_list(board, valid_coordinates)
    return pr_combined_list


def test_first_step(parameter_combined_list):
    pr_combined_list = parameter_combined_list
    res = propose_best_coordinate_v2(pr_combined_list, 'x', board, valid_coordinates)
    assert res == 'b2'


def test_convert_from_math_to_game_coordinates():
    assert map_to_coordinates(1, 1) == 'b2'
    assert map_to_coordinates(4, 4) == '**'
    assert map_to_coordinates(0, 0) == 'a3'
    assert map_to_coordinates(2, 0) == 'a1'
    assert map_to_coordinates(2, 5) == '*1'
    assert map_to_coordinates(5, 2) == 'c*'


def test_convert_to_math_from_game_coordinates():
    assert map_from_coordinates('b2') == (1, 1)
    assert map_from_coordinates('**') == (-1, -1)
    assert map_from_coordinates('c3') == (0, 2)
    assert map_from_coordinates('a3') == (0, 0)
    assert map_from_coordinates('a1') == (2, 0)
    assert map_from_coordinates('c*') == (-1, 2)


def test_create_combined_lists():
    expected_result = [['a3.', 'b3.', 'c3.'], ['a3.', 'a2.', 'a1.'], ['a2.', 'b2.', 'c2.'],
                       ['b3.', 'b2.', 'b1.'], ['a1.', 'b1.', 'c1.'], ['c3.', 'c2.', 'c1.'],
                       ['a3.', 'b2.', 'c1.'], ['a1.', 'b2.', 'c3.']]
    assert create_combined_list(board, valid_coordinates) == expected_result


def test_select_lists_with_possible_coordinates(parameter_combined_list):
    combined_list = parameter_combined_list
    select_list = select_lists_with_possible_coordinates(combined_list, 'x')
    expected_list = [['a3.', 'b3.', 'c3.'], ['a3.', 'a2.', 'a1.'], ['a2.', 'b2.', 'c2.'],
                     ['b3.', 'b2.', 'b1.'], ['a1.', 'b1.', 'c1.'], ['c3.', 'c2.', 'c1.'],
                     ['a3.', 'b2.', 'c1.'], ['a1.', 'b2.', 'c3.']]
    assert select_list == expected_list


def test_round_for_computer():
    # b_1 = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    res = play_round_for_computer(board_1, True, valid_coordinates)
    assert res == 'b2'


def test_play_computer_round():
    # b_1 = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    res = play_computer_round(board_1, 'x', valid_coordinates)
    assert res == 'b2'


def test_cross_list(parameter_combined_list):
    combined_list = parameter_combined_list
    select_list = select_lists_with_possible_coordinates(combined_list, 'x')
    flat_list = cross_lists(select_list, 2)
    assert flat_list == ['a3.', 'b3.', 'c3.', 'a3.', 'a2.', 'a1.', 'a2.', 'b2.', 'c2.', 'b3.', 'b2.', 'b1.', 'a1.', 'b1.', 'c1.', 'c3.', 'c2.', 'c1.', 'a3.', 'b2.',
                         'c1.', 'a1.', 'b2.', 'c3.']


def test_propose_best_coordinates(parameter_combined_list):
    combined_list = parameter_combined_list
    dict_max_keys = propose_best_coordinate(combined_list, 'x')
    assert dict_max_keys == ['b2']

    combined_list = [['a3x', 'b3.', 'c3.'], ['a3x', 'a2.', 'a1.'], ['a2.', 'b2o', 'c2.'],
                     ['b3.', 'b2o', 'b1.'], ['a1.', 'b1.', 'c1.'], ['c3.', 'c2.', 'c1.'],
                     ['a3x', 'b2o', 'c1.'], ['a1.', 'b2o', 'c3.']]
    dict_max_keys = propose_best_coordinate(combined_list, 'x')
    assert dict_max_keys == ['c2', 'b1', 'a1', 'c1', 'c3']

    combined_list = [['a3x', 'b3.', 'c3o'], ['a3x', 'a2o', 'a1x'], ['a2o', 'b2o', 'c2x'],
                     ['b3.', 'b2o', 'b1.'], ['a1x', 'b1.', 'c1.'], ['c3o', 'c2x', 'c1.'],
                     ['a3x', 'b2o', 'c1.'], ['a1x', 'b2o', 'c3o']]
    dict_max_keys = propose_best_coordinate(combined_list, 'x')
    assert dict_max_keys == ['b3', 'b1']

    combined_list = [['a3.', 'b3.', 'c3.'], ['a3.', 'a2.', 'a1.'], ['a2.', 'b2x', 'c2.'],
                     ['b3.', 'b2x', 'b1.'], ['a1.', 'b1.', 'c1.'], ['c3.', 'c2.', 'c1.'],
                     ['a3.', 'b2x', 'c1.'], ['a1.', 'b2x', 'c3.']]
    dict_max_keys = propose_best_coordinate(combined_list, 'x')
    assert dict_max_keys == ['a3', 'c3', 'a1', 'c1']

    combined_list = [['a3.', 'b3.', 'c3.'], ['a3.', 'a2.', 'a1x'], ['a2.', 'b2o', 'c2.'],
                     ['b3.', 'b2o', 'b1.'], ['a1x', 'b1.', 'c1.'], ['c3.', 'c2.', 'c1.'],
                     ['a3.', 'b2o', 'c1.'], ['a1x', 'b2o', 'c3.']]
    dict_max_keys = propose_best_coordinate(combined_list, 'x')
    assert dict_max_keys == ['a3', 'b3', 'c3', 'c2', 'c1']


def test_propose_best_coordinates_v2(parameter_combined_list):
    combined_list = parameter_combined_list
    res = propose_best_coordinate_v2(combined_list, 'x', board, valid_coordinates)
    assert res == 'b2'


def test_flip_token():
    assert flip_token('x') == 'o'
    assert flip_token('o') == 'x'


def test_is_free_square_present(foo):
    assert is_free_square_present(board_1) is True

    b = [['x', 'x', 'o'], ['o', 'o', 'x'], ['x', 'x', 'o']]
    assert is_free_square_present(b) is False

    b = [['.', 'x', 'o'], ['o', 'o', 'x'], ['x', 'x', 'o']]
    assert is_free_square_present(b) is True

    b = [['z', 'x', 'o'], ['o', 'o', 'x'], ['x', 'x', 'o']]
    assert is_free_square_present(b) is False


def test_computer_must_find_win_in_one_move_when_exists():
    b = [['x', '.', 'x'], ['.', '.', '.'], ['.', '.', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_computer_win_in_one_move(combined_list, 'o') == 'b3.'

    b = [['.', '.', '.'], ['x', 'x', '.'], ['.', '.', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_computer_win_in_one_move(combined_list, 'o') == 'c2.'

    b = [['.', '.', 'x'], ['.', '.', 'x'], ['x', 'x', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_computer_win_in_one_move(combined_list, 'o') == 'c1.'

    b = [['.', '.', 'x'], ['x', '.', ''], ['.', 'x', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_computer_win_in_one_move(combined_list, 'o') is None

    b = [['x', '.', '.'], ['x', '.', '.'], ['.', '.', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_computer_win_in_one_move(combined_list, 'o') == 'a1.'

    b = [['x', '.', '.'], ['.', 'x', '.'], ['.', '.', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_computer_win_in_one_move(combined_list, 'o') == 'c1.'

    b = [['.', 'x', '.'], ['.', 'x', '.'], ['x', '.', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_computer_win_in_one_move(combined_list, 'o') == 'b1.'


def test_computer_must_find_win_in_one_move_when_non_exists():
    b = [['.', '.', 'x'], ['x', '.', ''], ['.', 'x', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_computer_win_in_one_move(combined_list, 'o') is None


def test_computer_must_prevent_human_win_in_one_move_when_exists():
    b = [['x', '.', 'x'], ['.', '.', '.'], ['.', '.', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_human_win_in_one_move(combined_list, 'x') == 'b3.'

    b = [['x', 'x', '.'], ['.', 'x', '.'], ['x', '.', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_human_win_in_one_move(combined_list, 'x') == 'c3.'

    b = [['x', '.', '.'], ['.', 'x', '.'], ['.', '.', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_human_win_in_one_move(combined_list, 'x') == 'c1.'

    b = [['.', 'x', '.'], ['.', 'x', '.'], ['.', '.', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_human_win_in_one_move(combined_list, 'x') == 'b1.'

    b = [['.', '.', '.'], ['.', 'x', '.'], ['.', '.', 'x']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_human_win_in_one_move(combined_list, 'x') == 'a3.'

    b = [['x', 'x', '.'], ['.', 'x', '.'], ['x', '.', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_human_win_in_one_move(combined_list, 'x') == 'c3.'


def test_computer_must_prevent_human_win_in_one_move_when_non_exists():
    b = [['.', '.', 'x'], ['x', '.', '.'], ['.', 'x', '.']]
    combined_list = create_combined_list(b, valid_coordinates)
    assert is_human_win_in_one_move(combined_list, 'x') is None


def test_is_free_of_enemy_tokens():
    combined_list = [['a3.', 'b3.', 'c3.'], ['a3.', 'a2.', 'a1.'], ['a2.', 'b2.', 'c2.'],
                     ['b3.', 'b2.', 'b1.'], ['a1.', 'b1.', 'c1.'], ['c3.', 'c2.', 'c1.'],
                     ['a3.', 'b2.', 'c1.'], ['a1.', 'b2.', 'c3.']]
    assert is_free_of_enemy_token(combined_list, 'x', 'b2') is True

    combined_list = [['a3x', 'b3.', 'c3o'], ['a3x', 'a2o', 'a1x'], ['a2o', 'b2o', 'c2x'],
                     ['b3.', 'b2o', 'b1.'], ['a1x', 'b1.', 'c1.'], ['c3o', 'c2x', 'c1.'],
                     ['a3x', 'b2o', 'c1.'], ['a1x', 'b2o', 'c3o']]
    assert is_free_of_enemy_token(combined_list, 'x', 'b1') is True

    combined_list = [['a3o', 'b3.', 'c3.'], ['a3o', 'a2.', 'a1.'], ['a2.', 'b2x', 'c2.'],
                     ['b3.', 'b2x', 'b1.'], ['a1.', 'b1.', 'c1x'], ['c3.', 'c2.', 'c1x'],
                     ['a3o', 'b2x', 'c1x'], ['a1.', 'b2x', 'c3.']]
    assert is_free_of_enemy_token(combined_list, 'x', 'a1') is True


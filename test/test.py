# w, h = 3, 3
# matrix = [["."]*w]*h
# print(matrix)
# win_combinations = [
#     ["a1", "a2", "a3"],
#     ["b1", "b2", "b3"],
#     ["c1", "c2", "c3"],
#     ["a1", "b1", "c1"],
#     ["a2", "b2", "c2"],
#     ["a3", "b3", "c3"],
#     ["a1", "b2", "c3"],
#     ["a3", "b2", "c1"]
# s = [['ss1', 'ss2', 'ss6'],['ss3','ewqe','fsdfs']]
# for g in s:
#     for h in g:
#         if '3' not in h:
#            pass
# ]    while (True):
#         coordinate = accept_coordinate()
#         if is_valid(coordinate):
#             play_round(board, coordinate, 'x')
#         else:
#             coordinate = second_try()
#print("debug", board[len(board)-1-row_index][col_index], coord_names[len(coord_names)-1-row_index][col_index])
# ss = [ 'a1', 'A1', 'B1', 'b1']
# for coord in ss:
#     if coord.isupper():
#         print(coord)
# [["A3", "a3",  "b3", "c3"], ["A2", "a2", "B2", "b2", "C2", "c2"], ["A1", "a1", "B1", "b1", "C1", "c1"] ]
# wrong_array = [['a1x', 'a2.', 'a3.'], ['b1.', 'b2x', 'b3.'],['c1.', 'c2.','c3o']]
# human_token = 'x'
# right_array =[]
# index = 0
# ll = [['a1.', 'a2x' , 'a3o'], ['b1.', 'b2x', 'b3.'],['c1.', 'c2.','c3o'],['c1.', 'c2.','c3o']]
# for l in ll:
#     print(l[0])
#     index += 1
    # for el in l:
    #     if el[2].count(human_token) == 0:
    #         right_array.append(l)
    #         index += 1
# for list in wrong_array:
#     for el in list:
#         print('ss')
#     if list[index][2].count(human_token) == 0:
#         right_array.append(list)
#         index += 1

    # for element in list:
    #     if element[2].count(human_token) == 0:
    #             right_array.append(element)
# print(right_array)
# for s in ss:
#     for i in s:
#         if i != 'x':
#             print(1)
#         else:
#             print(2)
# if len(set(triple)) != '.' :
# if triple.count(triple[0]) != '.' and  triple.count(triple[0])== len(triple) :
# if all(triple) != '.':
# array = [ "Alex", "Bob", "Bob", "John"]
#
# array_d = dict.fromkeys(array, 0)
# for a in array:
#     array_d[a] += 1
# mas = array_d.get
# print(mas)
#
# max_key = max(array_d, key=array_d.get)
# print(max_key)
# x = 'x.'
# x = x + '.'
# print(x)
# dic = {90373544:5 , 905043:4 , 444445:1 , 234235:2, 245435:5}
# max_val = max(dic.values())
# print([k for k,v in dic.items() if v == max_val])
list_1 = [[2, 3, 3, 5, 6]]
list2 = [e.copy() for e in list_1]
list2[0][2] = 4
print(list_1)
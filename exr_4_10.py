from os import lstat


def number_in_list(lst, target):
    new_lst = sorted(lst)
    res_lst = []
    for i in range(len(lst)):
        if new_lst[i] == target:
            res_lst.append(i)
    if res_lst == []:
        return [-1, -1]
    return res_lst

print(number_in_list([7, 7, 8, 5, 9, 8], 12))
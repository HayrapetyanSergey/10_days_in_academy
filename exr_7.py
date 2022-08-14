def pow_lst(lst, n):
    new_lst = [None] * len(lst)
    for i in range(len(lst)):
        new_lst[i] = lst[i] ** n
    sorted_lst = sorted(new_lst)
    return sorted_lst

print(pow_lst([1, 3, 4, 5, 2], 2))
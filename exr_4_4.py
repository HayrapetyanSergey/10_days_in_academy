def even_sorted(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            new_lst.append(lst[i])
    for i in range(len(lst)):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
    return new_lst

print(even_sorted([1,2,3,4]))
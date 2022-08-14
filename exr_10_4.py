def arr(lst):
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            return lst[i]
            break
    return -1

print(arr([1, 2, 4, 1, 2]))        
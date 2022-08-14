def arr(lst):
    for i in range(len(lst)):
        if lst.count(lst[i]) > 1:
            return True
            break
    return False

print(arr([1, 2, 3, 3]))        
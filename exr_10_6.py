def one(lst):
    count = 0
    new_lst = []
    for i in range(len(lst)):
        if lst[i] == 1:
            count += 1
        else: 
            count = 0
    return count

print(one([1, 1, 0, 1, 0, 1, 1]))
def less_num(lst):
    for j in range(len(lst)):
        for i in range(len(lst)):
            if j != lst[i]:
                return j

print(less_num([0, 3, 2]))
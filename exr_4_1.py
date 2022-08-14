def pop_push(target, n):
    lst = [None] * n
    res = [None] * n
    for i in range(1, n + 1):
        lst[i - 1] = i
    for k in range(len(res)):
        if lst[k] in target:
            res[k] = 'push'
        else:
            res[k] = 'pop'
    return res

print(pop_push([1, 2, 3], 4))
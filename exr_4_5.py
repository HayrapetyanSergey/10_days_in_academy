def sum_of_unique(lst):
    return sum(lst[i] for i in range(len(lst)) if lst.count(lst[i]) == 1)

print(sum_of_unique([1, 2, 3, 4, 5]))
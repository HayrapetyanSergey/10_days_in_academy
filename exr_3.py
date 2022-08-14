dict_of_values = {}
lst  = [1, 2, 3, 2]
for i in range(len(lst)):
    dict_of_values[lst[i]] = lst.count(lst[i])
print(dict_of_values)    
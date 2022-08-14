def two_list(lst1, lst2):
    lst = [] 
    for i in range(max(len(lst1), len(lst2))):
        if lst1[i] in lst2 and lst1[i] not in lst:
            lst.append(lst1[i])
    return lst

print(two_list([1, 2, 1, 3, 2, 5, 8], [5, 2, 3, 4, 2, 1]))
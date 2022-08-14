def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)- i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([3, 2, 1, 5, 4]))
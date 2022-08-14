def number_is_polindrom(n):
    return str(n) == str(n)[::-1]

lst = []
lst1 = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if number_is_polindrom(i * j):
            lst.append(i * j)
            lst1.append(i)

print(max(lst))
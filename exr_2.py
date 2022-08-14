with open("second.txt", "r") as f:
    res = [row.title() for row in f.readline()]

with open('new_second.txt', 'w') as f:
    for row in res:
        f.write(row)
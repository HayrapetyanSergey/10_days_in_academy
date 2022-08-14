source_code = []
res = 0
with open("first.txt", "r") as f:
    file_code = [row.strip() for row in f.readlines()]
    for i in range(len(file_code)):
        file_code[i] = file_code[i].split()
    for i in range(len(file_code)):
        file_row = file_code[i]
        for l in range(len(file_row)):
            res += int(file_row[l])

print(res)
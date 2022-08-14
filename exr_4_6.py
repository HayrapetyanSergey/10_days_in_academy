def search_str(str, sear):
    count = 0
    for i in range(len(str)):
        for j in range(len(sear)):
            if str[i] == sear[j]:
                count += 1
                break
    return count

print(search_str('hello', 'll'))                 
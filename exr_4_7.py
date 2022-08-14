def last_word(str):
    lst = str.split(' ')
    lst1 = lst[-1]
    return len(lst1)

print(last_word('Hello world'))
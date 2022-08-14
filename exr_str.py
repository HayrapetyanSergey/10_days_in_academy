def str_move(string, count):
    return string[-count:] + string[:-count]
    
print(str_move("hello", 2))    
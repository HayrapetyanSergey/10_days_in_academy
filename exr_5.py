def delete_simvol(string):
    count = 0
    new_string = ''
    for i in range(len(string)):
        if string[i].isalpha():
            count += 1
        if count % 3 == 0:
            pass
        else:
            new_string += string[i]    
    return new_string

print(delete_simvol('Hatyanstkan'))               
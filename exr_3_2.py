with open("name.txt", "r") as file:
    for contents in file.readlines():
        name = contents.title()

with open("new_name.txt", "w") as n_file:
    for contents in name:
        n_file.write(contents)
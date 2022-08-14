def count_of_odd_number(start, end):
    count = 0
    for i in range(start, end + 1):
        if i % 2 == 1:
            count += 1
    return count

print(count_of_odd_number(-8,6))
def difference(n):
    sum = 0
    mult = 1
    for digit in str(n):
        sum += int(digit)
        mult *= int(digit)
    return mult - sum

number = 4637
print(difference(number))
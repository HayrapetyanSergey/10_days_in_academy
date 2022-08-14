def diff(n):
    sum = 0
    sum_of_sq = 0
    for i in range(1, n + 1):
        sum += i
        sum_of_sq += i ** 2
    return sum_of_sq - sum

print(diff(100))    
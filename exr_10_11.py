def sums(n):
    sum1 = 0
    sum2 = 0
    for i in range(1, n + 1):
        sum1 += i ** 2
        sum2 += i
    return sum1 - (sum2 ** 2)

print(sums(100))
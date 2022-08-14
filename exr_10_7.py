def arrayPairSum(nums):
    nums_sort = sorted(nums)
    res = 0
    i = 0
    while i < len(nums):
        res += nums_sort[i]
        i += 2
    return res

print(arrayPairSum([6, 2, 6, 5, 1, 2]))
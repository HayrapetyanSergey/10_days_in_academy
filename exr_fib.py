def iseven(n):
    return n % 2 == 0
    
def fib(n):
    list_of_fib_numbers = []
    cache_0, cache_1, cache_next = 0, 1, 0
    while cache_next < n:
        cache_next = cache_0 + cache_1
        cache_0 = cache_1
        cache_1 = cache_next
        if iseven(cache_next):
            if cache_next < n:
                list_of_fib_numbers.append(cache_next)
    return sum(list_of_fib_numbers)

print(fib(4000000))    
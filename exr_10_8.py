def is_prime(n):
  for i in range(2,n):
    if (n % i) == 0:
      return False
  return True

def big_prime(num):
    lst = []
    for i in range(1, num):
        if (num % i) == 0 and is_prime(i):
            lst.append(i)
    return max(lst)

print(big_prime(60085143))
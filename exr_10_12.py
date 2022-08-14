def is_prime(n):
  for i in range(2,n):
    if (n % i) == 0:
      return False
  return True

def nthPrime(n):
    number_of_primes = 0
    prime = 1
    while number_of_primes < n:
        prime += 1
        if is_prime(prime):
            number_of_primes += 1
    return prime

print(nthPrime(10001))
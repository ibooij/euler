import math

def is_prime(n, primes):
    if n < 2:
        return False
    
    max = math.ceil(math.sqrt(n))
    for p in primes:
        if n % p == 0:
            return False

    return True

def n_th_prime(n):
    primes = [2,3]
    i = 5
    while len(primes) < n:
        if is_prime(i, primes):
            primes.append(i)
        i += 2

    if len(primes) % 20 == 0:
        print len(primes)
    return primes

print n_th_prime(10001)[-1]
    
                    

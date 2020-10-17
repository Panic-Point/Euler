import time
import math

INPUT = 2000000


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
            if n % i == 0:
                return False
    return True


def gen_primes(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    return primes


start = time.time()
print(sum(gen_primes(INPUT)))
print("--- %s seconds ---" % (time.time() - start))

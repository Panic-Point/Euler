import time

primes = [2]


def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True


def gen_primes(n):
    check = 3
    while len(primes) < n:
        if is_prime(check):
            primes.append(check)
        check += 2


start = time.time()
gen_primes(10001)
print(primes.pop())
print("--- %s seconds ---" % (time.time() - start))


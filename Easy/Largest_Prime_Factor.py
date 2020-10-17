import math

INPUT = 600851475143


def is_prime(n):
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


for j in range(int(math.ceil(math.sqrt(INPUT))), 0, -1):
    if INPUT % j == 0 and is_prime(j):
        print(j)
        break

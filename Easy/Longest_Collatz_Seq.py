import time

def collatz(n):
    out = n // 2 if n % 2 == 0 else 3 * n + 1
    return out


def gen_seq(n):
    count = 0
    while n != 1:
        count += 1
        n = collatz(n)
    return count + 1


start = time.time()
max_len = 0
max_coll = 1
for i in range(2, 1000001):
    coll = gen_seq(i)
    if coll > max_len:
        max_coll = i
        max_len = coll
total_time = time.time() - start
print(max_coll, max_len, total_time)

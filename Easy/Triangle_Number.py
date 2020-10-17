import math


def countDivisors(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                cnt = cnt + 1
            else:
                cnt = cnt + 2

    return cnt


t_num = 1
count = 2

while countDivisors(t_num) < 500:
    t_num += count
    count += 1

print(t_num)

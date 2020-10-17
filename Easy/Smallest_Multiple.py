import math
INPUT = 20
l = sorted(list(range(1, INPUT + 1)), reverse=True)

check = []
ans = 2520

for x in l:
    add = True
    for y in check:
        if y % x == 0:
            add = False
            break
    if add:
        check.append(x)

while True:
    factor = False
    for n in check:
        factor = True
        if ans % n != 0:
            factor = False
            break
    if factor:
        print(ans)
        exit()
    else:
        ans += 2



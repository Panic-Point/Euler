def is_triplet(t: tuple):
    return t[0]**2 + t[1]**2 == t[2]**2


for a in range(1, 998):
    for b in range(1, 998):
        c = 1000 - a - b
        if is_triplet((a, b, c)):
            print(a, b, c)
            print(a*b*c)
            exit()

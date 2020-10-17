ans = 0

def is_palindrome(n):
    s = str(n)
    r = s[::-1]
    if r == s:
        return True
    return False


for x in range(999, 901, -1):
    for y in range(999, 901, -1):
        if is_palindrome(x*y):
            print(x*y)
            exit()



"""
Memoization
https://towardsdatascience.com/memoization-in-python-57c0a738179a
 Memoization is a method used in computer science to speed up calculations by storing (remembering) past calculations.
 If repeated function calls are made with the same parameters, we can store the previous values instead of repeating
 unnecessary calculations.
"""

even_fib = []
fib_cache = {1: 1, 2: 1}
ans = 0
i = 3


def gen_fib_numbers(input_value):
    if input_value in fib_cache:
        return fib_cache[input_value]
    else:
        val = fib_cache[input_value - 1] + fib_cache[input_value - 2]
    fib_cache[input_value] = val
    if val % 2 == 0 and val < 4000000:
        even_fib.append(val)
    return val


# for i in range(3, 10):
#     print("fib({}) = ".format(i), gen_fib_numbers(i))

while ans < 4000000:
    ans = gen_fib_numbers(i)
    i += 1

print(even_fib)
print(sum(even_fib))

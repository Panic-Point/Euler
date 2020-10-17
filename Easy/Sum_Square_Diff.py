def sum_of_square(n):
    ans = 0
    for i in range(1, n + 1):
        ans += i ** 2
    return ans


def square_of_sums(n):
    ans = sum(list(range(1, n+1))) ** 2
    return ans


print(abs(square_of_sums(100) - sum_of_square(100)))

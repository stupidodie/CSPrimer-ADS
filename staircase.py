def f(n):
    a, b, c = 1, 1, 2
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a


assert f(4) == 7
assert f(5) == 13

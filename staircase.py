def f(n: int):
    assert n > 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return f(n - 1) + f(n - 2) + f(n - 3)


assert f(4) == 7
assert f(5) == 13

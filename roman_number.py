parts = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def f(n):
    for d, r in parts:
        if d <= n:
            return r + f(n - d)
    return ""


if __name__ == "__main__":
    cases = ((39, "XXXIX"), (2421, "MMCDXXI"), (1066, "MLXVI"))
    for n, x in cases:
        assert f(n) == x
    print("ok")

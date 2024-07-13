def lint(input_file: str) -> None:
    left_pares = ["(", "[", "{"]
    right_pares = [")", "]", "}"]
    pares = []
    with open(input_file, "r") as f:
        for line_no, line in enumerate(f):
            for char in line:
                if char in left_pares:
                    pares.append(left_pares.index(char))
                if char in right_pares:
                    if len(pares) == 0:
                        print(f"Face not matched pares on line {line_no} char {char}")
                    else:
                        expected_char = right_pares[pares.pop()]
                        if expected_char != char:
                            print(
                                f"Face not matched pares on line {line_no} char {char} expected {expected_char}"
                            )
                        else:
                            pass
        if len(pares) != 0:
            print(f"Not empty stack {pares}")


def pare_match(str):
    left_pares = ["(", "[", "{"]
    right_pares = [")", "]", "}"]
    pares = []
    for char in str:
        if char in left_pares:
            pares.append(left_pares.index(char))
        if char not in right_pares:
            continue
        try:
            last_value = pares.pop()
        except IndexError:
            return False
        expected_char = right_pares[last_value]
        if expected_char != char:
            return False
    return len(pares) == 0


def test_matched_cases():
    assert pare_match("[]") is True
    assert pare_match("()") is True
    assert pare_match("{}") is True
    assert pare_match("{()}") is True
    assert pare_match("{([])}") is True
    assert pare_match("{]") is False
    assert pare_match("({}]") is False

    print("All Test passed")


if __name__ == "__main__":
    test_matched_cases()
    # lint("./stretch.rkt")

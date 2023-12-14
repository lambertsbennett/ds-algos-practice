def find_factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        return n * find_factorial(n - 1)


def test_find_factorial():
    ans = find_factorial(2)
    assert ans == 2
    ans = find_factorial(3)
    assert ans == 6

def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def test_fib():
    ans = fib(1)
    assert ans == 1
    ans = fib(3)
    assert ans == 2
    ans = fib(8)
    assert ans == 21

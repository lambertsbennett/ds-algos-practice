def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_iterator(n: int) -> int:
    vals = [0, 1]
    if n == 0:
        return vals[0]
    elif n == 1:
        return vals[1]
    else:
        i = 1
        while i < n:
            vals.append(vals[0] + vals[1])
            _ = vals.pop(0)
            i += 1
        return vals[1]


def test_recursive_fib():
    ans = fib(1)
    assert ans == 1
    ans = fib(3)
    assert ans == 2
    ans = fib(8)
    assert ans == 21


def test_iterative_fib():
    ans = fib_iterator(1)
    assert ans == 1
    ans = fib_iterator(8)
    assert ans == 21

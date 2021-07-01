def fib_simple(n: int):
    a, b = 0, 1
    for _ in range(n):
        b, a = a + b, b
    return a


fib_rec = lambda n: fib_rec(n - 1) + fib_rec(n - 2) if n > 2 else 1

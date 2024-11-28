def f(n: int) -> int:
    if n <= 1:
        return 1
    return f(n - 1) * n

print(f(eval(input())))
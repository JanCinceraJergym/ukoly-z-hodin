# Fibonacciho posloupnost

from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap


# rekurzivní
@timing
def f1(n: int) -> int:
    return f_rek(n)

def f_rek(n: int) -> int:
    if n <= 2:
        return 1
    return f_rek(n-1) + f_rek(n-2)

# iterativní
@timing
def f2(n: int) -> int:
    a = 1
    a_prev = 0
    tmp = 0
    for _ in range(n-1):
        tmp = a_prev
        a_prev = a
        a = tmp + a
    return a

n = int(input())
print(f1(n))
print(f2(n))
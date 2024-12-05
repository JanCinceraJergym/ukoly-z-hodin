import sys

if len(sys.argv) <= 1:
    exit(-1)
filename = sys.argv[1]

with open(filename, "r") as ipf:
    T = int(ipf.readline())
    for _ in range(T):
        N = int(ipf.readline())
        A = list(map(int, ipf.readline().split()))

        f = {}
        for k in A:
            if k in f:
                f[k] += 1
            else:
                f[k] = 1

        m = 0
        for k in f:
            if f[k] > m:
                m = f[k]

        print(m)

import sys

if len(sys.argv) <= 1:
    exit(-1)
filename = sys.argv[1]

T = 0
with open(filename, "r") as ipf:
    T = int(ipf.readline())
    for _ in range(T):
        (N, X, Y, K) = map(int, ipf.readline().split())
        #print(f"N: {N},\tX: {X},\tY: {Y},\tK: {K}")
        if K*X <= Y:
            print(N*X)
        else:
            n1 = N//K
            n2 = N - (n1*K)
            if n2*X > Y:
                print(n1 * Y + Y)
            else:
                print(n1 * Y + n2*X)

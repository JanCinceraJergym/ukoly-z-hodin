T = 0
problems = []
with open("karticky.txt", "r") as ipf:
    T = int(ipf.readline())
    for _ in range(T):
        problems.append(map(int, ipf.readline().split()))

for (N, X, Y, K) in problems:
    #print(f"N: {N},\tX: {X},\tY: {Y},\tK: {K}")
    if K/Y <= 1/X:
        print(N*X)
    else:
        n1 = N//K
        n2 = N - (n1*K)
        print(n1 * Y + n2*X)

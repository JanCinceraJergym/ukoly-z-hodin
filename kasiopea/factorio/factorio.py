import sys

if len(sys.argv) <= 1:
    exit(-1)
filename = sys.argv[1]

with open(filename, "r") as ipf:
    T = int(ipf.readline())
    for _ in range(T):
        N = int(ipf.readline())
        S = list(map(int, ipf.readline().split()))

        a = []
        tmp = []
        prev = -1
        for n in S:
            if prev == 0:
                prev = n
            prev = n
            if n == 0:
                a.append(tmp)
                tmp = []
            else:
                tmp.append(n)
        a.append(tmp)

        print(f"-> {a}")

        total = 0
        for l in a:
            even = 0
            odd = 0
            for (i, k) in enumerate(l):
                if i % 2 == 0:
                    even += k
                else:
                    odd += k
            if even > odd:
                total += even
            else:
                total += odd

        print(total)
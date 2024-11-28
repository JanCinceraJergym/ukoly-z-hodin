T = 0
with open("knihy.txt", "r") as ipf:
    T = int(ipf.readline())
    for _ in range(T):
        N = int(ipf.readline())
        shelf = ipf.readline().removesuffix("\n")
        if shelf.count("K") <= 1:
            print(0)
            continue
        first_K = shelf.find("K")
        last_K = shelf.rfind("K")
        print(shelf[first_K:last_K].count("_"))
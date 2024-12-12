def is_safe(report: list[int]) -> bool:
    last = report[0]
    decreasing = report[0] > report[1]
    for level in report[1:]:
        diff = level - last
        if decreasing and (diff >= 0 or diff < -3):
            return False
        elif not decreasing and (diff <= 0 or diff > 3):
            return False
        last = level
    return True
            
safe_reports = 0

with open("input.txt", "r") as ipf:
    while True:
        line = ipf.readline()
        if line == "":
            break
        report = list(map(int, line.removesuffix("\n").split()))
        if is_safe(report):
            safe_reports += 1

print(safe_reports)
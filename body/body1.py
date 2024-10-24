import math, sys

k_input_text = "k = "
point_input_text = "point(x, y): "
stdin_file = False

if not sys.stdin.isatty():
    k_input_text = ""
    point_input_text = ""
    stdin_file = True

input_k = eval(input(k_input_text))

points = []

while True:
    try:
        s = input(point_input_text)
        if s == "":
            break
        x, y = eval(s)
        points.append((x, y))
    except EOFError:
        if not stdin_file:
            print()
        break

if len(points) == 0:
    if not stdin_file:
        print("No points specified.")
    exit(-1)

def line(a, x, b):
    return a*x + b

def line_const(x, y, a):
    return y - a*x

def count_points(c):
    up = 0
    down = 0
    for (x, y) in points:
        if y > line(input_k, x, c):
            up += 1
        elif y < line(input_k, x, c):
            down += 1
    return (up, down)


c_max = -math.inf
c_min = math.inf

for (x, y) in points:
    c = line_const(x, y, input_k)
    if c < c_min:
        c_min = c
    elif c > c_max:
        c_max = c

#print(f"c is in <{round(c_min, 2)}; {round(c_max, 2)}>")

up, down = -1, 1
result_c = float("nan")
while up != down:
    last_c = result_c
    result_c = (c_max + c_min) / 2
    if result_c == last_c:
        print("No solution.")
        exit(-1)
    up, down = count_points(result_c)
    #print(f"c = {round(result_c, 3)} \tup: {up}\tdown: {down}")
    if up > down:
        c_min = result_c
    elif up < down:
        c_max = result_c

if stdin_file:
    print(result_c)
else:
    print(f"c = {result_c}")



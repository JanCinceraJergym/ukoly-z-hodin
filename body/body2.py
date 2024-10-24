import math
#import matplotlib.pyplot as plt

import math, sys

k_input_text = "k = "
point_input_text = "point(x, y): "
stdin_file = False

if not sys.stdin.isatty():
    k_input_text = ""
    point_input_text = ""
    stdin_file = True

k = eval(input(k_input_text))

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

def rotate_point(point, angle):
    return (point[0]*math.cos(angle)-point[1]*math.sin(angle), point[0]*math.sin(angle)+point[1]*math.cos(angle))

points2 = []

alpha = math.atan(k)

for p in points:
    points2.append(rotate_point(p, -alpha))

#fig, ax = plt.subplots()

#for i, point in enumerate(points):
#    ax.plot(*point, "ro")
#    plt.text(point[0], point[1]+0.2, "{}: ({:.2f}, {:.2f})".format(i, point[0], point[1]))

points2.sort(key=lambda p: p[1])
if len(points2)%2 == 0:
    x = (points2[len(points2)//2][0] + points2[len(points2)//2-1][0])/2
    y = (points2[len(points2)//2][1] + points2[len(points2)//2-1][1])/2
else:
    x = points2[len(points2)//2][0]
    y = points2[len(points2)//2][1]


m = (x, y)
h = rotate_point(m, alpha)

c = h[1] - k*h[0]
print(c)

#ax.set_aspect(aspect=1)
#plt.axline((0, c), (1, k+c))
#ax.set_ylim(bottom=-7, top=7)
#ax.set_xlim(left=-7, right=7)
#ax.spines["left"].set_position("center")
#ax.spines["bottom"].set_position("center")
#ax.spines["right"].set_color("none")
#ax.spines["top"].set_color("none")
#ax.xaxis.set_ticks_position("bottom")
#ax.yaxis.set_ticks_position("left")
#plt.show()

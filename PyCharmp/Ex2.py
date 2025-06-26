import math


def cal_distance(l1, l2):
    x1, y1 = l1
    x2, y2 = l2

    return math.sqrt((x2 - x1) ** 2+(y2 - y1) ** 2)

l1 = (1, 2)
l2 = (4, 6)
print(cal_distance(l1, l2))
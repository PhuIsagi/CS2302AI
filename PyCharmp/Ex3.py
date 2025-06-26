def man_distance(l1, l2):
    x1, y1 = l1
    x2, y2 = l2
    return abs(x1 - x2) + abs(y1 - y2)

l1 = (1, 1)
l2 = (4, 5)

print(man_distance(l1, l2))
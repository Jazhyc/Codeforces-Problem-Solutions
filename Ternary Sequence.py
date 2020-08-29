t = int(input())

for _ in range(t):

    score = 0
    a0, b1, c2 = [int(x) for x in input().split()]
    x0, y1, z2 = [int(x) for x in input().split()]

    min1 = min(c2, y1)
    score += 2 * min1
    c2 -= min1
    y1 -= min1

    minx = min(b1, x0)
    b1 -= minx
    x0 -= minx

    min2 = min(b1, y1)
    b1 -= min2
    y1 -= min2

    min3 = min(a0, z2)
    a0 -= min3
    z2 -= min3

    min4 = min(b1, z2)
    score -= 2 * min4

    print(score)
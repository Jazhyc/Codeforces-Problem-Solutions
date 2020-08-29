from math import ceil, sqrt
t = int(input())

for i in range(t):

    a, b = [int(x) for x in input().split()]
    print(min(max(2 * a, b), max(2 * b, a)) ** 2)
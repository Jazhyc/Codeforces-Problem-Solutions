n = int(input())
c = 0
min = 0
for i in range(n):
    a, b = [int(x) for x in input().split()]
    c -= a
    c += b
    if min < c:
        min = c
print(min)
from math import floor
x = int(input())
n = 0
n += floor(x / 5)
if x % 5 != 0:
    n += 1
print(n)


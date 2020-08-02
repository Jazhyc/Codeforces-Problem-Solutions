from sys import stdin
from math import ceil
n = int(input())
alist = []
blist = []
for i in range(n):
    vals = stdin.readline()
    a, b = [int(x) for x in vals.split()]
    alist.append(a)
    blist.append(b)

for i, j in zip(alist, blist):
    print((ceil(i / j) * j) - i)
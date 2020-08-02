from math import inf
n = int(input())
soldiers = [int(x) for x in input().split()]
min = inf
max = -inf
for i in range(n):
    if soldiers[i] <= min:
        mindex = i
        min = soldiers[i]
    if soldiers[i] > max:
        maxdex = i
        max = soldiers[i]

if maxdex > mindex:
    mindex += 1

count = maxdex + n - mindex - 1
print(count)

# > and >= can make a big difference
# First Occurence, last occurence
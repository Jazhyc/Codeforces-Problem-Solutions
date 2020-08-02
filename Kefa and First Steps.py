from math import inf
n = int(input())
numbers = [int(x) for x in input().split()]
count = tcount = 0
max = -inf

for num in numbers:
    if num >= max:
        count += 1
        max = num
    else:
        if count >= tcount:
            tcount = count
        count = 1
        max = num

if tcount > count:
    print(tcount)
else:
    print(count)
from math import ceil
nums = input().split()
n, m, a = [int(x) for x in nums]
print(ceil(n/a) * ceil(m/a))
import bisect
n = int(input())
shops = [int(x) for x in input().split()]
shops.sort() # Expensive
for _ in range(int(input())):
    m = int(input())
    print(bisect.bisect_right(shops, m))

# Bisect_right returns index where item can be inserted without disturbing order
# Useful for some binary search problems
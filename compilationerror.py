n = int(input())
a = sum([int(x) for x in input().split()])
b = sum([int(x) for x in input().split()])
c = sum([int(x) for x in input().split()])

print(a - b)
print(b - c)

# Think Simple, lists differ by one element and duplicates might be present
# So just consider sums
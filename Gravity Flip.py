n = int(input())
columns = [int(x) for x in input().split()]
columns.sort()
print(' '.join(str(x) for x in columns))

# Short hand works in [] and ()
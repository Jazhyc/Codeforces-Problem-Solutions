n = int(input())
friends = [int(x) for x in input().split()]
gifts = [0 for x in range(n)]

for i in range(n):
    gifts[friends[i] - 1] = i + 1 
print(' '.join(str(x) for x in gifts))
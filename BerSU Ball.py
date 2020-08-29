b = int(input())
boys = [int(x) for x in input().split()]
g = int(input())
girls = [int(x) for x in input().split()]
boys.sort()
girls.sort()

count = 0

for i in range(b):
    for j in range(g):
        if abs(boys[i] - girls[j]) <= 1:
            girls[j] = float('inf')
            count += 1
            break
print(count)

# Girl with lowest skill is considered, does not effect answer
t = int(input())

for _ in range(t):

    n = int(input())
    aths = [int(x) for x in input().split()]
    aths.sort()

    diff = float('inf')

    for i in range(n - 1):

        if aths[i + 1] - aths[i] < diff:
            diff = aths[i + 1] - aths[i]
    
    print(diff)
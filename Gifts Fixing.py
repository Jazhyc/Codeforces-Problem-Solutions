for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    amin = min(a)
    bmin = min(b)
    count = 0

    for i, j in zip(a,b):
        count += max(i - amin, j - bmin)
    
    print(count)

# Iteration + logic = Success
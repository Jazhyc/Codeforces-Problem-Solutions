def solve(n, count):
    if n == 1:
        return count
    
    elif n % 6 == 0:
        return solve(n // 6, count + 1)
    
    elif n % 3 == 0:
        return solve(n * 2, count + 1)
    
    else:
        return -1

for _ in range(int(input())):
    n = int(input())
    count = 0
    print(solve(n, count))

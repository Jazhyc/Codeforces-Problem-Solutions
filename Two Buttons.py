n, m = [int(x) for x in input().split()]

def solve(n, m):

    if n >= m:
        return n - m
    elif m % 2 == 0:
        return 1 + solve(n, m // 2)
    else:
        return 2 + solve(n, (m + 1) // 2)

print(solve(n, m))

# Recursion allows dealing of cases within cases
# Reversing also helps
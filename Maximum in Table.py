n = int(input())

def solve(r,c):
    if r == 1 or c == 1:
        return 1
    return solve(r - 1, c) + solve(r, c - 1)

print(solve(n, n))

# Recursion + Trees = Fun
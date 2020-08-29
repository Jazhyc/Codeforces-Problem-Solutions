n, m, a, b = [int(x) for x in input().split()]

if (b / m) >= a:
    print(n * a)
else:
    print(((n // m) * b) + min(((n % m) * a), b))

# Neural Logic Module needs Updating
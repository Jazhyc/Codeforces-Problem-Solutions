for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    print(int((n * m + 1) / 2))

# If even nm, if odd 1 more than previous even number
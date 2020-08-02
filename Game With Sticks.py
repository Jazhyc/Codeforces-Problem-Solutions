n, m = [int(x) for x in input().split()]
a = min(m, n)

if a % 2 == 0:
    print("Malvika")
else:
    print("Akshat")

# Optimum way to win is to reduce one of the sides to 0
# Kind of an unfair game
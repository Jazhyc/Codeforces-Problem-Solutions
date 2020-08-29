n, r = [int(x) for x in input().split()]

for i in range(1, 11):
    if ((n * i) - r) % 10 == 0 or (n * i % 10) == 0:
        print(i)
        exit()

# Brackets are magic
# Edge Cases are not
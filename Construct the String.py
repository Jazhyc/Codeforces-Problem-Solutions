t = int(input())

for _ in range(t):

    n, a, b = [int(x) for x in input().split()]

    for i in range(n):
        print(chr(97 + i % b), end='')
    print()

# a is useless
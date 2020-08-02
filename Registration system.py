from sys import stdin
n = int(input())
mem = {}

for i in range(n):
    name = stdin.readline().split()[0]
    if name not in mem:
        mem[name] = 1
        print("OK")
    else:
        print(name + str(mem[name]))
        mem[name] += 1
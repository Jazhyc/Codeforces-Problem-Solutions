socks = [int(x) for x in input().split()]

if socks[0] >= socks[1]:
    n1 = socks[1]
    socks[0] -= n1
    n = 0
else:
    n1 = socks[0]
    socks[1] -= n1
    n = 1
    
print(n1, socks[n] // 2)
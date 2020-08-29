t = int(input())

for i in range(t):

    n = int(input())
    evec = oddc = 0
    arr = [int(x) for x in input().split()]

    for j in range(n):
        lhs = j % 2
        rhs = arr[j] % 2

        if lhs != rhs:
            if lhs == 0 and rhs == 1:
                oddc += 1
            else:
                evec += 1
    
    count = min(oddc, evec)

    if abs(oddc - evec) >= 1:
        print(-1)
    else:
        print(count)

t = int(input())

for _ in range(t):

    n = int(input())
    arr = [int(x) for x in input().split()]

    k = min(arr)
    arrc = arr.copy()
    arrc.sort()

    count = 0
    for i in range(n):
        if arr[i] % k == 0 or arrc[i] == arr[i]:
            count += 1
    
    if count == n:
        print('YES')
    else:
        print("NO")

# Proof by assumption
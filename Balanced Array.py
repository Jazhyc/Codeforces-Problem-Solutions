from sys import stdin
n = int(input())

for i in range(n):
    num = int(stdin.readline())

    if (num / 2) % 2 != 0:
        print("NO")
    
    else:
        print("YES")
        arr = []
        for i in range(2, num + 1, 2):
            arr.append(i)
        for i in range(0, num // 2 - 1):
            arr.append(1 + 2 * i)
        arr.append(sum(arr[:num // 2]) - sum(arr[num // 2:]))
        
        for num in arr:
            print(num, end=' ')
        print()
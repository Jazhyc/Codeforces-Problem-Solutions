for _ in range(int(input())):
    n = int(input())
    nums = []
    arr = [int(x) for x in input().split()]

    for i in arr:
        if i not in nums:
            nums.append(i)
    
    for i in nums:
        print(i, end=' ')
    print()
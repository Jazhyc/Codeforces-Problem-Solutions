k = int(input())

for i in range(k):
    num = [int(x) for x in list(input())]
    l = len(num)
    ans = []

    for j in range(l):
        if num[j] != 0:
            ans.append(num[j] * 10 ** (l - j - 1))

    print(len(ans))
    for k in ans:
        print(k, end =' ')
    print()
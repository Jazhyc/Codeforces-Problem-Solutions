from sys import stdin
n = int(input())

'''
GP Sum = (a * (1 - r ** n)) / (1 - r)
a = 1st term, r = common ratio, n = num
'''

for i in range(n):
    end = False
    num = int(stdin.readline())

    for k in range(2, 30):

        if (num % ((2 ** k) - 1)) == 0:
            print(num // (2 ** k - 1))
            break

# Linear Equations help
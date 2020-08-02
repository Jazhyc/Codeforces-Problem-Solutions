n = int(input())

for i in range(n):

    num = int(input())

    if num % 2 == 0:
        print(int(num / 2 - 1))
    else:
        print(int((num - 1) / 2))
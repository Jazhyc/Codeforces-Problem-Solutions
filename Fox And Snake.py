n, m = [int(x) for x in input().split()]
count = 0
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            print("#", end='')
        else:
            count += 1
            if count % 2 != 0:
                print('.' * (m - 1), end = '')
                print('#', end = '')
                break
            else:
                print('#', end = '')
                print('.' * (m - 1), end = '')
                break
    print()
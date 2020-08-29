n = int(input())
Mik = Chris = 0

for _ in range(n):
    m, c = [int(x) for x in input().split()]

    if m > c:
        Mik += 1
    elif c > m:
        Chris += 1

if Chris > Mik:
    print('Chris')
elif Mik > Chris:
    print('Mishka')
else:
    print("Friendship is magic!^^")
from sys import stdin
n = int(input())
pmag = '-1'
count = 0

for i in range(n):
    cell = stdin.readline() # Savior
    temp = cell[0]
    if temp != pmag:
        count += 1
    pmag = temp
print(count)
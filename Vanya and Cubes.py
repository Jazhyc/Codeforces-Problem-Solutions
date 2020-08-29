# Summantion = n / 2 * (a + an)
n = int(input())
count = 1
s = 1

i = 2
while s <= n:
    s += ((i * (i + 1)) / 2)
    count += 1
    i += 1

print(count - 1)
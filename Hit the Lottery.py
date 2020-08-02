n = int(input())
bills = [100, 20, 10, 5, 1]
count = 0

for bill in bills:
    if n % bill >= 0 and n != 0:
        count += n // bill
        n = n % bill

print(count)
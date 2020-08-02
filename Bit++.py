n = int(input())
ops = []
x = 0
for i in range(n):
    ops.append(input())

for op in ops:
    
    if op.count('+') == 2:
        x += 1

    elif op.count('-') == 2:
        x -= 1
print(x)
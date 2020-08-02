n1 = input()
n2 = input()
op = ''
for i, j in zip(n1, n2):
    if int(i) + int(j) in [0, 2]:
        op += '0'
    else:
        op += '1'
print(op)


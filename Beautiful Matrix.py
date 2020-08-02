from sys import exit
matrix = []
for i in range(5):
    matrix.append(input().split())

for i in range(5):
    for j in range(5):
        if matrix[i][j] == '1':
            print(abs(i - 2) + abs(j - 2))
            exit(0)
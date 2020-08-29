n = int(input())
students = input().split()
skills = {}
skills['1'], skills['2'], skills['3'] = [], [], [] # Python Wierdness

for i in range(n):
    skills[students[i]].append(i + 1)

P = len(skills['1'])
M = len(skills['2'])
PE = len(skills['3'])

m = min(P, M, PE)
print(m)
for i in range(m):
    print(skills['1'].pop(), skills['2'].pop(), skills['3'].pop())


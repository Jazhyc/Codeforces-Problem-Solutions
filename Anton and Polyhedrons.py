from sys import stdin
mapping = {
    'Tetrahedron': 4,
    'Cube' : 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron' : 20
}
n = int(input())
count = 0

for i in range(n):
    shape = stdin.readline()
    count += mapping[shape[:-1]]
print(count)
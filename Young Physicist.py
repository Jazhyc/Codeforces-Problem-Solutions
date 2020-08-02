n = int(input())
forces = []
x = y = z = 0

for i in range(n):
    forces.append([int(x) for x in input().split()])

for force in forces:

    x += force[0]
    y += force[1]
    z += force[2]

if x == y == z == 0:
    print("YES")
else:
    print("NO")
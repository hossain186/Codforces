n = int(input())
total = 0
for i in range(n):

    s = input()
    if s == "Icosahedron":
        total+=20
    elif s == "Cube":
        total +=6
    elif s == "Tetrahedron":
        total+=4
    elif s == "Dodecahedron":
        total +=12
    elif s == "Octahedron":
        total += 8

print(total)
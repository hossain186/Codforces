a = input()
b = input()
name2 = input()

ar2 = []
for i in name2:
    ar2.append(i)
ar2.sort()


total = a+b
ar = []

for i in total:
    ar.append(i)

ar.sort()
if ar == ar2:
    print("YES")
else:
    print("NO")
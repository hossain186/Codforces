name = input()

upper = 0
lower = 0

for i in name:

    if i.islower():
        lower+=1
    else:
        upper+=1

if upper <= lower:
    name = name.lower()
    print(name)
else:
    name = name.upper()

    print(name)





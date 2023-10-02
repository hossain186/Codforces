n = input()
total = ''
for i in n:

    if (i == "I" or i=='i' or i =='o' or i =='O' or
            i =='A' or i =="a" or i== 'Y' or i == 'y' or
            i == 'e' or i== 'E' or i == 'U' or i== 'u') :

        continue

    else:
        total+='.'+i

print(total.lower())

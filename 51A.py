n1 = input()
n2 = input()
n = ''

for i in range(len(n1)):

    if n2[i]!=n1[i]:
        n+='1'
    else:
        n+="0"


print(n)
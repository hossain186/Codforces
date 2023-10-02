
t = int(input())
total = []

for i in range(t):

    a,b = map(int, input().split( ' '))

    if a<b:
        x = b-a

    else:
        x = a%b
        if x == 0:
            x =0
        else:
            x= b-x
    total.append(x)

for n in total:
    print(n)
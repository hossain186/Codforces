a,b = input().split(' ')
a = int(a)
b= int(b)
i = 0

while True:

    if a>b:
        print(i)
        break

    else:
        a*=3
        b*=2

    i+=1

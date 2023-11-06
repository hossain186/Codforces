number = int(input())
for i in range(number):

    a,b,c,d = map(int, input().split(' '))
    n = [a,b,c,d]
    t = 0

    for i in n[1:]:
        if n[0]<i:
            t+=1
    print(t)
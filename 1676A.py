n = int(input())

for _ in range(n):

    a = int(input())

    d = a//1000

    c = a%1000

    n = str(d)
    n2 = str(c)

    l = [i for i in n]
    l1 = [i for i in n2]

    t1 = 0
    t2 = 0

    for i in l:
        t1+= int(i)

    for i in l1:
        t2+= int(i)

    if t1 == t2:
        print('YES')
    else:
        print("NO")
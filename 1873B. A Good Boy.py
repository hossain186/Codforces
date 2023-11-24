
m = int(input())

for _ in range(m):
    le = int(input())
    n = list(map(int,input().split(" ")))[0:le]


    max = 0
    for i in range(len(n)):

        x = n[i] + 1

        for j in range(len(n)):



            if i == j:
                continue
            else:
                x*=n[j]



        if max<x:
            max = x



    print(max)
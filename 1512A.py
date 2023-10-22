n = int(input())
li = 0
while li<n:

    index = int(input())
    a = list(map(int,input().split(' ')))
    result = 0
    for i in a[0:index]:

        if a.count(a[0]) == 1:
            result = 1

        else:

            for j in range(1,len(a)):
                if a[0] != a[j]:
                    result = j+1

    print(result)

    li +=1
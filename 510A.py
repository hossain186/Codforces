n,m = map(int, input().split(' '))


result = ''
for i in range(1,n+1):
    if i%4 == 0:
        result = "."* (m-1)

        print("#"+result)

    elif i%2 ==0:
        result = "." * (m-1)

        print(result+"#" )

    else:
        print("#"*m)
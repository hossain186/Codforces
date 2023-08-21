n = int(input())

x = 0
y = 0
z = 0

for i in range(n):
    ar = map(int, input().split(" "))
    ar = list(ar)

    x += ar[0]
    y +=ar[1]
    z +=ar[2]

if x == 0 and y==0 and z == 0 :
    print('YES')

else:
    print("NO")



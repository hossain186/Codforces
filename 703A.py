n = int(input())

t1 = 0
t2 = 0
for _ in range(n):
    a,b = map(int, input().split(' '))


    if a>b:
        t1+=1
    elif a<b:
        t2+=1

if t1>t2:
    print("Mishka")
elif t2>t1:
    print("Chris")
else:
    print("Friendship is magic!^^")
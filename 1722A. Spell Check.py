a = "Timur"
a=sorted(a)
n = int(input())

for _ in range(n):

    l = int(input())
    s = input()[0:l]

    if sorted(s)==a:
        print('YES')
    else:
        print("NO")


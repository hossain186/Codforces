n = int(input())

for _ in range(n):

    l = input()

    s = "abc"
    a = l[0]
    b = l[1]
    c = l[2]

    if a + b + c == s:
        print("YES")
    elif a + c + b == s:
        print("YES")
    elif b + a + c == s:
        print("YES")
    elif c + b + a == s:
        print("YES")

    else:
        print("NO")

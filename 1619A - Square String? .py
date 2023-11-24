n = int(input())
for _ in range(n):
    s = input()

    if len(s)%2 !=0:
        print("No")
    else:
        mid = len(s)//2
        if s[0:mid] == s[mid:]:
            print("YES")
        else:
            print("NO")


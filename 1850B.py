t = int(input())
for _ in range(t):

    new = []
    n = int(input())
    for i in range(n):
        a,b = map(int, input().split(" "))

        if a<= 10:
            new.append(b)
        else:
            new.append(0)
    result = max(new)
    print(new.index(result)+1)
j = 0
ind = 0
l = []
for i in range(5):

    n = list(map(int, input().split()))

    l.append(n)


for i in l:
    if 1 in l[j]:
        ind = abs(2-l[j].index(1))

        break

    j+=1

result = abs(2-j)+ind
print(result)

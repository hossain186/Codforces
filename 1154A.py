a = list(map(int, input().split(' ')))
a.sort(reverse=True)

n = a[0]

for i in a[1:]:
    print(n-i)
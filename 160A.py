n = int(input())
a = list(map(int, input().split(' ')))

total = 0
a.sort()
a.reverse()

for i in range(n):
    total+=a[i]



total2  = 0

for i in range(n+1):

    if total2 > total//2:
        print(i)
        break
    total2+=a[i]

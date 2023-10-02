m = map(int, input().split(' '))
m = list(m)
m.sort()
j= 0
final= ''
for i in m:
    i = str(i)

    final+=i+" "
    j+=1

print(final)
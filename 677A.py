n, h = map(int, input().split(' '))

num = input().split(' ')
total = 0
for i in num:

    i = int(i)

    if i <= h:
        total+=1
    else:
        total+=2


print(total)
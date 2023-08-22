
x, y = input().split(' ')
x = int(x)
y = int(y)
total = 0
for i in range(y):

     if x%10 == 0:
         x = x/10
     else:
         x = x-1


     total = x

print('{:.0f}'.format(total))


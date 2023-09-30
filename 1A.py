n,m,a = map(int, input().split(' '))
row= 0
col = 0

if n % a == 0:
    row = n // a

else:
    row = n // a + 1

if m % a == 0:
    col = m // a

else:
    col = m // a + 1


print(row*col)


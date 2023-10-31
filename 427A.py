n, k, l, c, d, p, nl, np = map(int, input().split(' '))

a = l*k

b = a//nl
lime = c*d
solt = p//np


retult = min(b,lime,solt)
print(retult//n)
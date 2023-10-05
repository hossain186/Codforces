a = int(input())
b = int(input())
c = int(input())

n = max(a+b+c, a*b*c, (a+b)*c , a*(b+c), a+b*c, a*b+c)
print(n)
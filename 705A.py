n = int(input())

s1 = [' it ', ' that ']
s2 = ['I love' , 'I hate']

result = ''

for i in range(1,n+1):

    if i%2 == 0:
        result+=s2[0]
    else:
        result+=s2[1]

    if i==n:
        result+=s1[0]
    else:
        result+=s1[1]

print(result)
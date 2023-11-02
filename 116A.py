n = int(input())


list = []
result = 0
for i in range(n):

    a,b = map(int, input().split(' '))

    result += (b-a)
    list.append(result)

print(max(list))



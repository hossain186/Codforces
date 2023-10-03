n = int(input())
room = 0



for i in range(n):
    a,b = map(int, input().split(' '))


    if b-a>=2:
        room+=1
    else:
        room+=0

print(room)

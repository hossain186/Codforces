n = int(input())
sum = 0

for i in range(n):
    x,y,z = input().split(" ")

    if (int(x) == 1 and int(y) == 1) or (int(z) == 1 and int(y))==1 or (int(z)==1 and int(x) ==1) :
        sum +=1


print(sum)


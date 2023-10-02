number = int(input())
n = input()

total1 = 0

j = 0


for i in n:

    if n[j] == n[j-1]:
        if j>=1:
            total1+=1
    else:
        total1+=0


    j+=1

print(total1)
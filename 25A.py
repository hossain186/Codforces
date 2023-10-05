n= int(input())

num =list(map(int, input().split(' ')))

odd = 0
even = 0

for i in num:
    if i%2==0:
        even+=1
    else:
        odd+=1

if even>odd:
    for i in num:
        if i%2!=0:
            print(num.index(i)+1)
            break
else:
    for i in num:
        if i%2==0 :
            print(num.index(i)+1)
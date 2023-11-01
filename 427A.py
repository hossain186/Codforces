n = int(input())
a = list(map(int, input().split(" ")))
police = 0
crime = 0

if a[0]== -1:
    crime+=1
else:
    police+=a[0]


for i in range(1,len(a[0:n])):

    if a[i] == -1:
        if police>0:
            police-=1

        else:
            crime+=1

    else:
        police+=a[i]

print(crime)





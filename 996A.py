num = [1,5,10, 20, 100]
n = int(input())

j = -1
total = 0
while True:
    if n>=num[j]:

        total +=  (n//num[j])
        n = n%num[j]

    else:
        j-=1

    if n ==0 :
        break
print(total)


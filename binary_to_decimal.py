n = int(input())
rem = 0
total = ""

while True:

    if n ==1:
        total+='1'
        break

    elif n== 0:
        total+= '0'
        break

    else:

        rem = n%2

        total+= str(rem)







    n = n // 2


print(total[::-1])
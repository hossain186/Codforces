num = int(input())
n =[]
j = 0
total = 1
for i in range(num):
    a = input()

    n.append(a)


for i in n:

    if j == num-1:
        break

    else:
        if i == '10':
            if n[j-num+1] == '01':

                total+=1
            else:

                total+=0



        else:

            if n[j-num+1] == '10':

                total+=1
            else:

                total+=0




    j+=1

print(total)
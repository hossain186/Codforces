'''
name= []

for i in range(int(input())):


    name.append(input())

j= 0
for i in name:
    if j ==0:
        print('OK')
    else:

        if i in name[0:j]:

            print(i+str(j))
        else:
            print('OK')


    j+=1

'''


name = {}

for i in range( int(input())):

    num = input()

    if  num in name:
        print(num+str(name[num]))
        name[num]+=1


    else:
        print("OK")
        name[num] =1




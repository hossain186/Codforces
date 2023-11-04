import sys

n = int(input())

nums = [True for i in range(n+1)]
# initial indexing value 2
j = 2

while j*j<=n:

     if nums[j]== True:

         for i in range(j*j, n+1 , j):
             nums[i] = False
     j+=1
new =[]

for i in range(2, n+1):

    if nums[i]:
        pass
    else:
        new.append(i)





for i in range(len(new)-1):
    for j in range(len(new)-1):


        if new[i]+new[j] == n:
            print(new[i],new[j])
            sys.exit()


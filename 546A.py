k,n,w = input().split(' ')

k= int(k)
n = int(n)
w = int(w)


sum = 0

for i in range(1,w+1):
    sum += i*k



if sum< n:
    print(0)

else:

    print(sum-n)


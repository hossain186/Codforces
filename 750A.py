n,t = map(int, input().split(' '))

total_time = 0

h_time = 240-t


result = 0


for i in range(n+1):
    n_time = 5
    n_time*=i
    total_time+=n_time
    if total_time>h_time:
        pass
    else:
        result = i


print(result)


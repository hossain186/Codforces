x = input().strip("{},").split(", ")



n = set(x)
result = 0
for i in n:

    if '' in n:
        result = 0
    else:
        result+=1
print(result)

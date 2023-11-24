
a = int(input())

if a ==1:
    print(1)
else:
    result = 0
    final = 0
    for i in range(1,a+1):
        if result>a:

            break
        s = 0
        for j in range(1,i+1):
            s+=j

        result+=s

        final+=1

    print(final-1)

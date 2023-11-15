import  re

n = int(input())
for _ in range(n):
    st = ''
    for _ in range(8):


        a = input()

        c = re.compile(r'\w')
        b = c.search(a)
        if b is not None:
            st+=b.group()

    print(st)

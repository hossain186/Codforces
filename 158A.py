n , p = map(int,input().split(' '))
score = map(int, input().split(' '))
score= list(score)
total = 0
for i in score:

    if i>=score[p-1] and i != 0:
        total +=1

print(total)

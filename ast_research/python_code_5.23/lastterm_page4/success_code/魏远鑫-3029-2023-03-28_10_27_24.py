names=input().split(',')
scores=eval(input())
a=[]
for i in range(len(names)):
    score=scores[i]
    list=[names[i],score]
    a.append(list)
print(a)


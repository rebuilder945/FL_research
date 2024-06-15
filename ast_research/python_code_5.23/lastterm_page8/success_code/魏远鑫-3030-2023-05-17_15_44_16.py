names=input().split(',')
scores=eval(input())
a=[]
for i in range(len(names)):
    score=scores[i]
    list=[names[i],score]
    a.append(list)
    list.sort(lambda x:x[1])
print(a)

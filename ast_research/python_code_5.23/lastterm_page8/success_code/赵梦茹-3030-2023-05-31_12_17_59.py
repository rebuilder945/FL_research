name=input().split(',')
score=eval(input())
a=list(name)
c=[]
for i in range(len(a)):
    b=(a[i],score[i])
    c.append(list(b))
print(c)

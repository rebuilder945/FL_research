name=input().split(',')
score=input().split(',')
a=list(name)
c=[]
for i in range(len(a)):
    b=(a[i],int(score[i]))
    c.append(list(b))
c.sort(key=lambda x:x[1])
print(c)

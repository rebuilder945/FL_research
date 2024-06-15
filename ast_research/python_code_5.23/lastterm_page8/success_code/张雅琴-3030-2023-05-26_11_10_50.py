name=[str(n)for n in input().split(",")]
grade=eval(input())
a=len(name)
b=0
x1=[]
while a>0:
    x2=[]
    x2.append(name[b])
    x2.append(grade[b])
    x1.append(x2)
    a-=1
    b+=1
e=0
x3=[]
for i in x1:
    f=0
    for j in x1:
        if j[1]>i[1]:
            x3=x1[e]
            x1[e]=x1[f]
            x1[f]=x3
        f+=1
    e+=1
print(x1)

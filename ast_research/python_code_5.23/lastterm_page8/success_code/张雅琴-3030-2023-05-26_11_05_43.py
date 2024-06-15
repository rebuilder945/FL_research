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
for i in x2:
    f=0
    for j in x2:
        if j[1]>i[1]:
            x3=x2[e]
            x2[e]=x2[f]
            x2[f]=x3
        f+=1
    e+=1
print(x2)

#设置一个空的列表
#
a=eval(input())
b=[]
d=[]
for i in range(len(a)):
    if a[i]==0:
        b.append(a[i])
    elif a[i]!=0:
        d.append(a[i])
c=d+b
print(c)



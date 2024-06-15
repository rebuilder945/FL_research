a=eval(input())
b=0
v=[]
for i in a:
    if i==0:
        v.append(i)
if a.count(0)==0:
    print(a)
else:
    while a.count(0)>b:
        a.remove(0)
        c=a
print(c+v)


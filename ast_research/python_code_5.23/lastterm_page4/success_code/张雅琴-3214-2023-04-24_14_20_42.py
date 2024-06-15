a=eval(input())
b=[]
c=a.count(0)
d=[0]*c
for i in a:
    if i!=0:
        b.append(i)
if b!=[]:    
    e=b+d
    print(e)
else:
    print(d)

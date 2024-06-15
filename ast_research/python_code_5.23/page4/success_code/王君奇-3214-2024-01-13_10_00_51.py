x=eval(input())
m=[]
for i in x:
    if i==0:
        x.remove(0)
        m.append(0)
    x.extend(m)
print(x)

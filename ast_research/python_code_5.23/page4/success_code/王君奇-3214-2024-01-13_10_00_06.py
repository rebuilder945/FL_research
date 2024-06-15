x=eval(input())
m=[]
for i in x:
    if i==0:
        x.remove(i)
        m.append(i)
    x.extend(m)
print(x)

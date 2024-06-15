a=[1,0,2,0,3,0,4,0]
b=[]
for i in a:
    if i==0:
        b.append(i)
        a.remove(i)
print(a+b)


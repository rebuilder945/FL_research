a=input()
a=a.split(',')
b=input()
b=b.replace("[","").replace("]","")
b=b.split(',')
b=list(map(int,b))
m=[]
for x,y in zip(a,b):
    p=[]
    p.append(x) 
    p.append(y)
    m.append(p)
print(m)



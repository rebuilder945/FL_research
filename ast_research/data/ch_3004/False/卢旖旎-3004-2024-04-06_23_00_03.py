a=eval(input())
d=[]
e=[]
for x in a:
    for n in range(3,x):
        results=x%n
        if results==0:
            d.append(x)       
for i in a:
    if x==1:
        e.append(i)
    if i not in d:
        e.append(i)
print(e)

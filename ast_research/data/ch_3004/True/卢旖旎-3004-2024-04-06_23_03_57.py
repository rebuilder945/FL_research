a=eval(input())
d=[]
e=[]
for x in a:
    for n in range(2,x):
        results=x%n
        if results==0:
            d.append(x)       
for i in a:
    if i not in d and i !=1 and i!=0:
        e.append(i)
print(e)

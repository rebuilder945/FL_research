a=eval(input())
b=[]
c=[]
for x in a:
    for i in range(2,x):
        if x%i== 0:
            break
    else:
        b.append(x)
for i in b:
    if i!=0 and i!=1:
        c.append(i)
print(c)
        
   





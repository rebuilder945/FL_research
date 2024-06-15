a = list(eval(input()))
if 2 in a:
    a.remove(2)
else:
    pass
if 1 in a:
    a.remove(1)
else:
    pass
b=[]
c=[]
for x in a :
    for i in range(2,x):
        if x % i ==0:
            b.append(x)
            continue
    if not x in b:
        c.append(x)    
            
print(c)


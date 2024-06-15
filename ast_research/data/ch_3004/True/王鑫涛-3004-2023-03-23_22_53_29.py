a = list(eval(input()))
b=[]
c=[]
if 0 in a:
    a.remove(0)
else:
    pass
if 1 in a:
    a.remove(1)
else:
    pass
for x in a :
    for i in range(2,x):
        if x % i ==0:
            b.append(x)
            continue
    if not x in b:
        c.append(x)    
            
print(c)


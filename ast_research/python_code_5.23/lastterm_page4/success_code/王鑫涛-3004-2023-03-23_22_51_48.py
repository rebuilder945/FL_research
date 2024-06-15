a = list(eval(input()))
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


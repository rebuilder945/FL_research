a=eval(input())
b=[]
c=[]
for i in a:
    if i==0:
        b.append(i)
    elif i!=0:
        c.append(i)
for x in range (len(b)):        
 c.append(b[x])
print(c)

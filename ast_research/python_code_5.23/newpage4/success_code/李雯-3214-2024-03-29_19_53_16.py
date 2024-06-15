a=eval(input())
d=a.copy()
b=[]
for i in d:
    if i==0:
        b.append(i)
        a.remove(i)    
    else:
        continue
c=a+b
print(c)

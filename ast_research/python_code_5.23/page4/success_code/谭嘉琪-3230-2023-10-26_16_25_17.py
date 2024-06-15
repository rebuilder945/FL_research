a=eval(input())
b=max(a)
b1=str(b)
a.remove(b)
d=b1
for i in range(len(a)):
    c=max(a)
    a.remove(c)
    c1=str(c)
    d=d+c1    
b2=int(d)
print(b2)



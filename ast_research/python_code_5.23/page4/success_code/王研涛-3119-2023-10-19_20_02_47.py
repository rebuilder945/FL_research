a=eval(input())
c=a.copy()
for x in a:
    b=c.count(x)
    if b>1:
        while b>1:
            c.remove(x)
            b=b-1
print(c)
        

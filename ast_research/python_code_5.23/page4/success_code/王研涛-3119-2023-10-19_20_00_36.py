a=eval(input())
c=a
for x in a:
    b=a.count(x)
    if b>1:
        while b>1:
            c.remove(x)
            b=b-1
print(c)
        

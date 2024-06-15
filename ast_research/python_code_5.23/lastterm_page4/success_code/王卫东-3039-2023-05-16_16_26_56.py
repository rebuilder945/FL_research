a=eval(input())
b=max(a)
d=min(a)
c=a.copy()
for x in a:
    if x==b or x==d:
        c.remove(x)       
print(c)        

a=eval(input())
c=max(a)
d=min(a)
e=a.copy()
for i in a:
    if i==c or i==d:
        e.remove(i)
print(e)        



    

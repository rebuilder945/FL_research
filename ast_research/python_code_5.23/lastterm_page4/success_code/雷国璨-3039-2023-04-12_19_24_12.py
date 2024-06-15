a=eval(input())
a1=max(a)
a2=min(a)
for i in a:
    if i==a1 or i==a2:
        a.remove(i)
    else:
        pass
print(a)
    

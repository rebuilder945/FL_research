a=eval(input())
a1=max(a)
a2=min(a)
b=a.copy()
for i in b:
    if i==a1 or i==a2:
        a.remove(i)
print(a)
    

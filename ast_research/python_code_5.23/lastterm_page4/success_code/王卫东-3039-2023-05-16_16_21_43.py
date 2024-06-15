a=eval(input())
b=max(a)
d=min(a)
for x in a:
    if x==b or x==d:
        a.remove(x)
for x in a:
    if x==b:
        a.remove(x)        
print(a)        

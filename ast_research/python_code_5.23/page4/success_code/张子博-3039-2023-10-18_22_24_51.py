k=eval(input())
i=max(k)
p=min(k)
m=k.count(i)
n=k.count(p)
if m>1:
    for u in range(m):
        k.remove(i)
if n>1:
    for b in range(n):
        k.remove(p)        
print(k)        

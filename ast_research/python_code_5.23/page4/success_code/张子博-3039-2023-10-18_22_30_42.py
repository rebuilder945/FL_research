k=eval(input())
i=max(k)
p=min(k)
m=k.count(i)
n=k.count(p)
for u in range(m):
        k.remove(i)
for b in range(n):
        k.remove(p)        
print(k)        

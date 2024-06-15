a=input()
ma=max(a)
mi=min(a)
s=len(a)
for i in range(s+1):
    a.remove(ma)
    a.remove(mi)
print(a)
    

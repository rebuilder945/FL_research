s=eval(input())
a=max(s)
a1=s.count(a)
b=min(s)
b1=s.count(b)
if a>b:
    for i in range(a1):
        s.remove(a)
    
    for x in range(b1):
        s.remove(b)
else:
    for i in range(a1):
        s.remove(a)
print(s)

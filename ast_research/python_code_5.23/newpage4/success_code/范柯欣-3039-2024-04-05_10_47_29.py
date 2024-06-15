a=list(eval(input()))
b=max(a)
c=min(a)
n1=a.count(b)
n2=a.count(c)
for i in range (n1):
    a.remove(b)
if len(a)>=1:
    for h in range (n2):
        a.remove(c)
print(a)

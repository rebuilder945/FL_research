a=eval(input())
b=a.copy()
c=max(a)
d=min(a)
for i in a:
    if i==c or i==d:
        b.remove(i)
print(b)


































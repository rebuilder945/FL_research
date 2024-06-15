a=eval(input())
b=a.copy()
for i in a:
    if i==0:
        b.remove(i)
c=b+[0]*a.count(0)
print(c)

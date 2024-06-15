a=eval(input())
lst=a.copy()
b=a.count(0)
c=[0]*b
for i in a:
    if i==0:
        b.remove(i)
d=b+c
print(d)

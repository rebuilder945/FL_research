a=eval(input())
b=a.count(0)
d=[]
for i in a:
    if i!=0:
        d.append(i)
for i in range(b):
    d.append(0)
print(d)

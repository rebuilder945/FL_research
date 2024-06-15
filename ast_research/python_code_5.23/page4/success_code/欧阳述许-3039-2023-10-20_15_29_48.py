a=eval(input())
b=max(a)
c=min(a)
d=[]
for x in a:
    if x==b or x==c:
       del x
d.append(a)
print(d)

a=eval(input())
c=[x for x in a]
c.reverse()
d=eval(c)
b=[]
for i in c:
    if i not in  b:
        b.append(i)
b.reverse()
print(b)

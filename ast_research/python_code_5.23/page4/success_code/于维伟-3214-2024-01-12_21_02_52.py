a=eval(input())
b=[]
for x in a:
    if x==0:
        b.append(x)
        a.pop(x)
a.append(b)
print(a)

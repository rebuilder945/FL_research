a=eval(input())
b=[]
for x in a:
    if x==0:
        b.append(x)
        a.remove(0)
for x in range(len(b)):
    a.append(0)
print(a)

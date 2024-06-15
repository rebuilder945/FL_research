a=eval(input())
b=[]
for x in a:
    if x==0:
        b.append(x)
        a.pop(x)
for x in range(len(b)):
    a.append(0)
print(a)

lst=eval(input())
n=list(range(2,100000,1))
m=[]
l=[]
for i in lst:
    for x in n:
        y=i/x
        if y in n:
            m.append(i)
for a in lst:
    if a not in m:
        l.append(a)
print(l)

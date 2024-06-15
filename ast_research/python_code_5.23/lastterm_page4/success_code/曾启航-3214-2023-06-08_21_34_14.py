a=input()
x=len(str(a))
i=0
while x>=0:
    if a[x]==0:
        a.pop(x)
        i+=1
        x-=1
    else:
        x-=1
while i>=0:
    a.append(0)
print(a)

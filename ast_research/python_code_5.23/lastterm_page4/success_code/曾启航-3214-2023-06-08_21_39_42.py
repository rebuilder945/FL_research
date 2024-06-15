a=input()
x=len(str(a)-1)
i=0
b=list(a)
while x>=0:
    if b[x]==0:
        a.pop(x)
        i+=1
        x-=1
    else:
        x-=1
while i>=0:
    a.append(0)
print(a)

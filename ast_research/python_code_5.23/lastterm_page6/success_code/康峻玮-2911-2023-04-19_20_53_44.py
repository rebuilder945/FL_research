ls=input().split(",")
for x in float(len(ls)):
    y=eval(ls[x])
    z=y+5
    d=str(z%10)
    d=ls[x]
i=0
while i<len(ls)/2-1:
    a=ls[i]
    b=ls[len(ls)-i-1]
    ls[i]=b
    ls[len(ls)-i-1]=a
    i=i+1
l=''.join(i for i in ls)
print(l)




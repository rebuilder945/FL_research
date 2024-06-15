a=eval(input())
b=[]
c=""
for i in range(0,len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
        b.sort()
if b==[]:
    print("False")
else:
    for i in range(0,len(b)):
        c=c+str(b[i])+","
        c=c[0,len(b)-1]
    print(c)

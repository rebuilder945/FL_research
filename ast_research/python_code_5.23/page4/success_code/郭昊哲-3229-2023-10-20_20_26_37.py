a=eval(input())
b=[]
for i in range(len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
    else:
        pass
b.sort(reverse=False)
if b==[]:
    print("False")
else:
    d=[]
    for i in range(len(b)):
        d.append(str(b[i]))
    print(",".join(d))










a=[1,2,3,5,2,3,4]
b=[]
for i in range(len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
if b==[]:
        print("False")
else:
    b.sort()
    b=list(map(str,b))
    print(",".join(b))



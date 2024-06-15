lst=eval(input())
new=[]
for x in lst:
    if lst.count(x)==1:
        new.append(x)
    else:
        pass
new.sort()
if len(new)!=0:
    for x in range(len(new)):
        str(new[x])
        print(",".join(new))
else:
    print("False")


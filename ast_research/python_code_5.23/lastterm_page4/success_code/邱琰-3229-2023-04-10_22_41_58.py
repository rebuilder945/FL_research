lst=eval(input())
new=[]
for x in lst:
    if lst.count(x)==1:
        new.append(x)
    else:
        pass
new.sort()
neew=[]
if len(new)!=0:
    for x in range(len(new)):
        neew.append(str(new[x]))
    print(",".join(neew))
else:
    print("False")

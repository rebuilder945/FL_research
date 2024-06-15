lst=eval(input())
lst0=[]
for x in lst:
    if lst.count(x)==1:
        lst0.append(x)
lst0.sort()
if len(lst0)==0:
    print("False")
elif len(lst0)>0:
    for x in lst0:
        print(",".join(str(x)),end="")

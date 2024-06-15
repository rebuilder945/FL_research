lst=eval(input())
new=[]
for x in lst:
    if lst.count(x)==1:
        new.append(x)
    else:
        pass
new.sort()
if len(new)!=0:
    str(new)
    new.remove('[')
    new.remove(']')
else:
    print("False")


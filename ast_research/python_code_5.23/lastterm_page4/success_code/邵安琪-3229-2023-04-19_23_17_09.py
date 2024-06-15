lst=eval(input())
a=set(lst)
b=[]
for x in a:
    if lst.count(x)==1:
        b.append(x)
b.sort()
if b ==[]:    
    print("False")
else:
    b=list(map(str,b))
    print(",".join(b))

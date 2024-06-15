lst=list(eval(input()))
b=[]
for i in lst:
    if lst.count(i)==1:
        b.append(i)
b.sort()
if len(b)>0:
    c=",".join(str(i)for i in b)
    print(c)
else:
    print("False")

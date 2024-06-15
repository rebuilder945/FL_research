lst=eval(input())
a=set(lst)
b=[]
for i in a:
    if lst.count(i)==1:
        b.append(i)
b.sort()
if b==[]:
    print("False")
else:
    b=list(map(str,b))
    print(",".join(b))

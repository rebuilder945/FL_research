a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(a)
b.sort()
if b==[]:
    print("False")
else:
    c=list(map(str,b))
    print(",".join(c))

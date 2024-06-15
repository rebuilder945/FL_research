a=eval(input())
b=[]
for i in a:
    if a.count(i)==1 and i not in b:
        b.append(i)
if len(b)>0:
    b.sort()
    print(",".join(b))
else:
    print("False")
    

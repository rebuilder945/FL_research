a=eval(input())
b=[]
for i in a:
    if a.count(i)==1 and i not in b:
        b.append(i)
if b!=[]:
    b.sort()
    c=map(str,b)
    print(",".join(c))
else:
    print("False")
    

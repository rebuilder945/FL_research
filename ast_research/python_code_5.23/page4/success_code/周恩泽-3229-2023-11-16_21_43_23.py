n1=eval(input())
n2=[]
for x in n1:
    if n1.count(x)==1:
        n2.append(x)
n2.sort()
print(",".join(str(x) for x  in n2))
if n2==[]:  
    print("False")



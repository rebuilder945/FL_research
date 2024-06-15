n1=eval(input())
n2=[]
for x in n1:
    if n1.count(x)==1:
        n2.append(x)
        n2.sort()
if n2==[]:
    print("False")
else: 
    a=",".join([str(i)for i in n2])
    print(a)


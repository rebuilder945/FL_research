n=eval(input())
a=[]
for i in n:
    if n.count(i)==1:
        a.append(i)
if a==[]:
    print("False")
else:
    a.sort()
    print(*a,sep=",")

    






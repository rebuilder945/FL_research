lst=eval(input())
a=[]
for i in lst:
    if lst.count(i)==1:
        a.append(i)
a.sort(reverse=False)
if a==[]:
    print("False")
else:
    print(*a,sep=",")

lst=eval(input())
a=[]
for i in lst:
    if lst.count(i)==1:
        a.append(i)
a.sort()
if a==[]:
    print("Flase")
else:
    print(*a,sep=",")

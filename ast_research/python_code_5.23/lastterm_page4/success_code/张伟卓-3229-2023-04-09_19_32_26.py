lst=eval(input())
set=set(lst)
new=[]
for i in set:
    if lst.count(i)==1:
        new.append(i)
new.sort()
if new==[]:
    print("False")
else:
    new=list(map(str,new))
    print("".join(new))

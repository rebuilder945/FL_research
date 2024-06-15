n=eval(input())
lst=[]
for i in n:
    if n.count(i)==1 :
        lst.append(i)
if len(lst)=0:
    print("False")
else:
    lst.sort()
    print(lst)

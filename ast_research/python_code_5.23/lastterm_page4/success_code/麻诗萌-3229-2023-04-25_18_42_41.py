n=eval(input())
lst=[]
for i in n:
    if n.count(i)==1 :
        lst.append(i)
if len(lst)==0:
    print("False")
else:
    lst.sort()
    lst0=[]
    for i in lst:
        lst0.append(str(i))
    print(','.join(lst0))    

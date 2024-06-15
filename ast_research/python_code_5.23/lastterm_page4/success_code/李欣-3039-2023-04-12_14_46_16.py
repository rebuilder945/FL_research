lst1=eval(input())
lst2=sorted(set(lst1))
lst4=[]
if len(lst2)==1 and len(lst2)==2:
    print(lst4)
else:
    a=lst2[0]
    b=lst2[-1]
    lst3=set(lst1)
    lst3.remove(a)
    lst3.remove(b)
    print(lst3)

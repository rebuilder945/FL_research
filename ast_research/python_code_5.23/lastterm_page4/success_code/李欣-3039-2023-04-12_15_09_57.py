lst1=eval(input())
lst2=sorted(lst1)
lst4=[]
if len(lst2)==1 and len(lst2)==2 and len(lst2)==0:
    print(lst4)
else:
    a=lst2[0]
    b=lst2[-1]
    if a==b:
        print(lst4)
    else:
        while lst1.count(a)>0:
            lst1.remove(a)
        while lst1.count(b)>0:
            lst1.remove(b)
    print(lst1)

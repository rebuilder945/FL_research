n=eval(input())
lst1=[]
lst2=[]
lst3=[]
if n>1 and type(n)==int:
    lst=[x for x in range(2,n)]
    for x in lst:
        if str(x)==str(x)[::-1]:
            lst1.append(x)
    for x in lst1:
        for y in range(2,x):
            if x%y==0:
                lst2.append(x)
    for x in lst1:
        if x not in lst2:
            lst3.append(str(x))
    print(" ".join(lst3))
else:
    print("illegal input")

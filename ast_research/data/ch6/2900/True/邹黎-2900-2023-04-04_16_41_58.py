a=eval(input())
lst1=[]
lst2=[]
lst3=[]
if a>0 and type(a)==int: 
    for x in range (1,a+1,1):
        for y in range(1,x+1,1):
            if x%y==0:
                lst1.append(x)
    for x in lst1:
        if lst1.count(x)==2:
            if x not in lst2:
                lst2.append(x)
    for x in lst2:
        if str(x)== str(x)[::-1] :
            lst3.append(str(x))
    print(" ".join(lst3))
else:
     print("illegal input")


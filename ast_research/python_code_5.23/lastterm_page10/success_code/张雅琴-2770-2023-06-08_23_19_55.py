a=input()
b=input()
if len(a)!=len(b):
    print("False")
else:
    lst1=[]
    lst2=[]
    for i in a:
        lst1.append(i)
    for j in b:
        lst2.append(j)
    num=0    
    for x in lst1:
        if lst1.count(x)!=lst2.count(x):
            num+=1
    if num==0:
        print("True")
    else:
        print("False")

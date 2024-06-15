a=input()
b=input()
lst1=[]
lst2=[]
if len(a)!=len(b):
    print("False")
else:
    for i in a:
        lst1.append(i)
    for i in b:
        lst2.append(i)
    lst1.sort()
    lst2.sort()
    if lst1==lst2:
        print("True")
    else:
        print("False")



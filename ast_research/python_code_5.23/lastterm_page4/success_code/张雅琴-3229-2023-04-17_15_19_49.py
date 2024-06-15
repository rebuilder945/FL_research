lst=eval(input())
lst1=[]
for i in lst:
    a=lst.count(i)
    a=int(a)
    if a==1:
        lst1.append(i)
        lst1.sort()
    print(str(lst1))
else:
    print("False")


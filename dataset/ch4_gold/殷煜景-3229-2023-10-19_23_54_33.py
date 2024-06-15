lst=eval(input())
lst1=[]
for i in lst:
    if lst.count(i)==1:
        lst1.append(i)
if lst1==[]:
    print("False")
else:
    print(lst1)


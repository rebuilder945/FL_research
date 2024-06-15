lst=eval(input())
lst1=[]
n=lst.count(0)
for i in lst:
    if i!=0:
        lst1.append(i)
lst2=[0]*n
lst3=lst1+lst2
print(lst3)


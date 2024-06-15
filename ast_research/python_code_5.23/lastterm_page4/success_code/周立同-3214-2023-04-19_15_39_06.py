lst=eval(input())
lst1=[]
lst2=[]
for i in lst:
    if i==0:
        lst2.append(i)
    else:
        lst1.append(i)
lst3=lst1+lst2
print(lst3)

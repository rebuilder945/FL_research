lst1=eval(input())
lst2=[]
lst3=[]
for i in lst1:
    if i!=0:
        lst2.append(i)
    else:
        lst3.append(i)
lst=lst2+lst3
print(lst)


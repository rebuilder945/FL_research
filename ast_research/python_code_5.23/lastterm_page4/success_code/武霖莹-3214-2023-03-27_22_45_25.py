lst=eval(input())
lst1=[]
lst2=[]
for x in lst:
    if x==0:
        lst2.append(x)
    else:
        lst1.append(x)
lst3=lst1+lst2
print(lst3)


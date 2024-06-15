lst=eval(input())
lst2=[]
lst3=[]
for i in lst:
    if i==0:
        lst2.append(i)
    else:
        lst3.append(i)
print(lst3+lst2)


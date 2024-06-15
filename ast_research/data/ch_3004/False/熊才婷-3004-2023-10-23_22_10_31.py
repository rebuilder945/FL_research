lst=eval(input())
lst1=[]
lst2=[]
lst3=[]
for i in lst:
    if i==2 or i==3:
        lst1.append(i)
    elif i>=4:
        for x in range(2,i):
            if i%x==0:
                lst1.append(i)
for j in lst:
    if j not in lst1:
        lst2.append(j)
for k in lst2:
    if k not in lst3:
        lst3.append(k)
print(lst3)

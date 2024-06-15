lst=eval(input())
lst1=[]
lst2=[]
for i in lst:
    if i==2 or i==3:
        lst1.append(i)
    elif i>=4:
        for x in range(2,i//2+1):
            if i%x==0:
                break
            lst1.append(i)
for j in lst1:
    if j not in lst2:
        lst2.append(j)
print(lst2)

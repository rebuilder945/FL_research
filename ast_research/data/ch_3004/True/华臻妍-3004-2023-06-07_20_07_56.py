lst=eval(input())
lst1=[]
for i in lst:
    if i==2:
        lst1.append(i)
    elif i!=0 and i!=1:
        for a in range(2,i):
            if i%a==0:
                break
        else:
             lst1.append(i)
print(lst1)
        

                 









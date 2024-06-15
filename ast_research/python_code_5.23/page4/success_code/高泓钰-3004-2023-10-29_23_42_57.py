lst=eval(input())
lst2=lst[:]
for i in lst:
    if  i==1:
        pass    
    else:
        for m in range(2,i):
            if i % m==0:
                lst2.remove(i)
               
print(lst2)





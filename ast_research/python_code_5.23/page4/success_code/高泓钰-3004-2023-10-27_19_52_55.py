lst=eval(input())
lst2=[]
for i in lst:
    if i==1 or i==2:
        lst2.append(i)
    else:
        for x in range(2,i):
            if i%x==0:
                break
        eles:lst2.append(i)

        
        
                

lst=eval(input())
lst2=[]
for i in lst:
    if lst.count(i)==1:
        lst2.append(i)
lst2.sort()
if lst2:
    print(",".join(str(i)for i in lst2))
else:
    print("False")


        
         
     

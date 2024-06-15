lst=eval(input())
lst2=lst.copy()
lst1=[]
for i in lst:
    if i==1 or i==0:
        lst2.remove(i)
    else:
        for q in range(2,i,1):
            if i%q==0 :
                lst2.remove(i)
                break       
print(lst2)

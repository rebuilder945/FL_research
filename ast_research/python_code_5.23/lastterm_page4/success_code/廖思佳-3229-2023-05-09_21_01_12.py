nums=eval(input())
list1=list(nums)
lst=[]
m=0
for x in list1 :
    if list1.count(x)==1:
        lst.append(x)
        m+=1
    else:
        continue
lst.sort()
k=""
for i in range(len(lst)-1):
    k=k+str(lst[i])+","  
k=k+str(lst[len(lst)-1])
if m==0:
    print(False)
else:
    print(k)
    

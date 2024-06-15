import numbers


nums=eval(input())
list1=list(nums)
lst=[]
for x in list1 :
    if list1.count(x)!=1:
        lst=lst
    if list1.count(x)==1:
        lst=lst+[x] 
if lst==[]:
    print(False)
else:

    lst.sort()
    k=""
    for i in range(len(lst)-1):
        k=k+str(lst[i])+","  

    k=k+str(lst[len(lst)-1])
    print(k)

nums=eval(input())
list1=list(nums)
lst=[]
m=0
for x in list1:
    if list1.count(x)==1:
        lst.append(x)
        m+=1
    else:
        continue
lst.sort()
if m!=0:
    print(lst)
else:
    print("False")

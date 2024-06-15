nums=eval(input())
lst=[]
for x in nums:
    if nums.count(x)>1:
        pass
    else:
        lst.append(x)
if len(lst)==0:
    print("False")
elif len(lst)>0:
    lst.sort()
    lsta=','.join(str(i)for i in lst)
    print(lst)

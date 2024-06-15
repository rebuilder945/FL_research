nums=eval(input())
list=[]
for x in nums:
    if nums.count(x) > 1:
        pass
    else:
        list.append(x)
if len(list)== 0:
    print("False")
else:
    list.sort()
    list1 = ','.join(str(i) for i in list)
    print(list1)

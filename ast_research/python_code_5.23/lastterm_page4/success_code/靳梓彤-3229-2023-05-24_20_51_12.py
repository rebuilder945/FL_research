nums=eval(input())
lst=[]
for i in nums:
    if nums.count(i)==1:
        lst.append(i)
lst.sort()
if lst:
    print(",".join(str(i) for i in lst))
else:
    print('False')

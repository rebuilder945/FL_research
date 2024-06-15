nums=eval(input())
alist=[]
for num in nums:
    if nums.count(num)==1:
        alist.append(num)
alist.sort()
if alist:
    print(",".join(str(i)for i in alist))
else:
    print("False")

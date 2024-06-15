nums=eval(input())
maxnum=max(nums)
minnum=min(nums)
new=nums.copy()
for i in nums:
    if i==maxnum or i==minnum:
        new.remove(i)
print(new)

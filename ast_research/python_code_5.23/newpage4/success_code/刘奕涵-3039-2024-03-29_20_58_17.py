nums=eval(input())
maxnum=max(nums)
minnum=min(nums)
tmp=nums.copy()
for num in nums:
    if num == maxnum or num == minnum:
        tmp.remove(num)
print(tmp)

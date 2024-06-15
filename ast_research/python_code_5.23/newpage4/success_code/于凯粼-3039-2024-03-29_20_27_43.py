nums=eval(input())
maxnum=max(nums)
minnum=min(nums)
numt=nums.copy
for num in nums:
    if num==maxnum or num==minnum:
        numt.remove(num)
print(numt)

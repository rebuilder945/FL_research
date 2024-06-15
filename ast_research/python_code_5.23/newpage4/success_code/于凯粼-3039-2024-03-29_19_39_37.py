nums=eval(input())
maxnum=max(nums)
minnum=min(nums)
num=nums.copy
for num in nums:
    if num==maxnum or num==minnum:
        num.remove(num)
print(num)

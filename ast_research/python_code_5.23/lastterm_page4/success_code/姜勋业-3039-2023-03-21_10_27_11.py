nums=eval(input())
nums.sort()
for i in nums[0:len(nums)]:
    if i==nums[0] :
       del nums[i]
for x in nums[len(nums):0]:
    if x==nums(len(nums)):
        del nums[x]
print(nums)

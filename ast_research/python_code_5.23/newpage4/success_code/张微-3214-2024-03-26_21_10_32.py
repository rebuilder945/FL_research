nums=eval(input())
# print(nums[0])
# print(len(nums))
for n in range(len(nums)-1):
    for i in range(1,len(nums)):
        if nums[i-1]==0:
            t=nums[i]
            nums[i]=nums[i-1]
            nums[i-1]=t
print(nums)



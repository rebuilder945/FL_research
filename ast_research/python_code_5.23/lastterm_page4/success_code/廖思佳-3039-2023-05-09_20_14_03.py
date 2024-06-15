nums=eval(input())
a=max(nums)
b=min(nums)
for i in range(len(nums)):
    if a==nums[i] or b==nums[i]:
        del nums[i]
print(nums)



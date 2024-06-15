nums=eval(input())
a=max(nums)
b=min(nums)
for i in range(len(nums)):
    if nums[i]==a or nums[i]==b:
        del nums[i]
print(nums)



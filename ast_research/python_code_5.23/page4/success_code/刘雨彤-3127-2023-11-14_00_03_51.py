n=eval(input())
nums=[num for n in range(n+1)]
for i in range(len(nums)):
    a=nums.pop(nums[0])
    nums.append(a)
print(nums)




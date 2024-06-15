def search(nums):
    for i in range(len(nums)):
        if nums.count(nums[i])>len(nums)/2:
            return nums[i]





nums = eval(input())
y = search(nums)
print(y)



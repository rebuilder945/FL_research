def search(nums):
    for i in nums:
        if nums.count(nums[i]) > len(nums)//2:
            a = nums[i]
        else:
            a = 'False'
    return a
        





nums = eval(input())
y = search(nums)
print(y)



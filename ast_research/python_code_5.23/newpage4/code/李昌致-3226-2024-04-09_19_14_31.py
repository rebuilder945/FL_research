def search(nums):
    a = 114514
    for i in nums:
        if nums.count(nums[i]) > len(nums)//2:
            a = nums[i]
    if a == 114514
        a = 'False'
    return a
        





nums = eval(input())
y = search(nums)
print(y)



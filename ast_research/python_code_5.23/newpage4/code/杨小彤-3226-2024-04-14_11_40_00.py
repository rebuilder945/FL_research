def search(nums):
    for x in nums:
        if nums.count(x)>=len(nums)//2):
            return nums[x]
        else:
            return False






nums = eval(input())
y = search(nums)
print(y)



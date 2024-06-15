def search(nums):
    for i in range(len(nums)):
        if nums.count(nums[i])>len(nums)/2:
            return nums[i]
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)



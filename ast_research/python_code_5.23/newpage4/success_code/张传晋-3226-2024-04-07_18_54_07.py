def search(nums):
    n = len(nums)
    for i in range(len(nums)):
        if nums.count(nums[i]) > n//2:
            d = nums[i]
            return d
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)



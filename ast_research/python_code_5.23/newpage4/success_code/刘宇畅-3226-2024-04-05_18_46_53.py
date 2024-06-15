def search(nums):
    a=len(nums)
    for i in range(0,a):
        if nums.count(nums[i])>a//2:
            return nums[i]
        if nums.count(nums[i])<=a//2:
            return False





nums = eval(input())
y = search(nums)
print(y)



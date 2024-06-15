def search(nums):
    for i in range(0,len(nums)):
        a=nums.count(nums[i])
        if a>(len(nums)/2):
            return nums[i]
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)



def search(nums):
    a = len(nums)/2
    b = 0
    for i in range(len(nums)):
        if nums.count(i) > a:
            b += nums[i]
            return b
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)



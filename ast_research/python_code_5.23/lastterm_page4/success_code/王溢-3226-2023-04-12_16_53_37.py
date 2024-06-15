def search(nums):
    for x in nums:
        if nums.count(x)>len(nums) // 2:
            return x
        else:
            return false





nums = eval(input())
y = search(nums)
print(y)



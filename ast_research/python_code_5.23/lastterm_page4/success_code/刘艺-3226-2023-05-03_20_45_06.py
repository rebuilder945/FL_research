def search(nums):
    for x in nums:
        if nums.count(x) > len(nums) / 2:
            d = x
        else:
            d = "false"
    return d





nums = eval(input())
y = search(nums)
print(y)



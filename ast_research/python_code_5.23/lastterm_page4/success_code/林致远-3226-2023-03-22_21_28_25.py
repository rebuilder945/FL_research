def search(nums):
    y = 0
    for x in nums:
        times = nums.count(x)
        if times > y:
            y = times
    if a <= len(nums)//2:
        y = False
    return y





nums = eval(input())
y = search(nums)
print(y)



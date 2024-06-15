def search(nums):
    t = 0
    for x in nums:
        times = nums.count(x)
        if times > t:
            y = x
            t = times
    if t <= len(nums)//2:
        y = False
    return y





nums = eval(input())
y = search(nums)
print(y)



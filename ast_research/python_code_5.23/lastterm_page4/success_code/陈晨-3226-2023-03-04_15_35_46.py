def search(nums):
    um=len(nums)
    for x in nums:
        if nums.count(x)>um//2:
            y=x
        else:
            pass
    return y





nums = eval(input())
y = search(nums)
print(y)



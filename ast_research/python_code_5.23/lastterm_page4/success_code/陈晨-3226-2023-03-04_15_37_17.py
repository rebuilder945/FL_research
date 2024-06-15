def search(nums):
    um=len(nums)
    for x in nums:
        if nums.count(x)>um//2:
            tt=x
        else:
            tt=false
    return tt





nums = eval(input())
y = search(nums)
print(y)



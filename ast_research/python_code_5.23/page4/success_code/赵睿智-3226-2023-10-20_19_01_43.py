def search(nums):
    n=len(nums)
    for x in nums:
        if nums.count(x)>n//2:
            h=x
        else:
            h="Flase"
    return h






nums = eval(input())
y = search(nums)
print(y)



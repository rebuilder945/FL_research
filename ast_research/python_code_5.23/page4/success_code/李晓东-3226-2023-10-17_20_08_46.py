def search(nums):
    for i in nums:
        if nums.count(i)>(n/2):
            x = nums.count(i)
        else:
            x = False
    return(x)
    





nums = eval(input())
y = search(nums)
print(y)



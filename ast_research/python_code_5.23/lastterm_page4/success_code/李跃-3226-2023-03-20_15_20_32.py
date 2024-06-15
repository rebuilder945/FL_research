def search(nums):
    n=len(nums)
    for x in nums:
        a=nums.count(x)
        if a>n//2:
            b=a
        else:
            b="False"
    return b
    





nums = eval(input())
y = search(nums)
print(y)



def search(nums):
    n=len(nums)
    for x in nums:
        t=nums.count(x)
        if t>n*0.5:
            d=x
        else:
            d="False"
    return d






nums = eval(input())
y = search(nums)
print(y)



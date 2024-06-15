def search(nums):
    a=len(nums)
    c=0
    for i in range(a):
        b=nums.count(i)
        if b >=a/2:
            c=nums[i]
    return c





nums = eval(input())
y = search(nums)
print(y)



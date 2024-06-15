def search(nums):
    a=len(nums)
    c=""
    for i in range(a):
        b=nums.count(i)
        if b >=a/2:
            c=nums[i]
            return c
    return False





nums = eval(input())
y = search(nums)
print(y)



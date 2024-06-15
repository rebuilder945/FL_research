def search(nums):
    n=len(nums)
    for x in nums:
        m=nums.count(x)
        if m>n/2:
            return m
    return False





nums = eval(input())
y = search(nums)
print(y)



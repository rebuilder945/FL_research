def search(nums):
    n=len(nums)
    for i in nums:
        d=nums.count(i)
        if d>n//2:
            return i
    return False





nums = eval(input())
y = search(nums)
print(y)



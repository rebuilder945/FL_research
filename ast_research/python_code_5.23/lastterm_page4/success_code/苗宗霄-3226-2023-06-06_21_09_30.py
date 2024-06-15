def search(nums):
    n=len(nums)
    for y in nums:
        x=nums.count(y)
        if x>n/2:
            return y
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)



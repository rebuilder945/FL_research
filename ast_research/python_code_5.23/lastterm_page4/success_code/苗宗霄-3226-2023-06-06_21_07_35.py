def search(nums):
    n=len(nums)
    for y in nums:
        nums.count(y)
        if y>n/2:
            return y
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)



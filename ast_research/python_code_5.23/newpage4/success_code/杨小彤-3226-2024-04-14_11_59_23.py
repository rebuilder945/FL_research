def search(nums):
    n = len(nums)
    for x in nums:
        if nums.count(x)>=(n//2):
            return x
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)



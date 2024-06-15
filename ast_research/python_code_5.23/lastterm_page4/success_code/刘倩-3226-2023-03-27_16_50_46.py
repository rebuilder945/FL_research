def search(nums):
    for x in nums:
        b = nums.count(x)
        n = len(nums)
        if b > (n//2):
            return x
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)



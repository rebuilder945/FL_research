def search(nums):
    n=len(nums)
    for i in nums:
        if i >(n//2):
            return i
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)



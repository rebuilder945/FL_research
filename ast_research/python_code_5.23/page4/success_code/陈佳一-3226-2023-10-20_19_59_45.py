def search(nums):
    n=len(nums)
    a=nums.count(x)
    for x in nums:
        if a>n//2:
            return a
        if a<=n//2:
            return False
      





nums = eval(input())
y = search(nums)
print(y)



def search():
    n=len(nums)
    for x in nums:
        a=nums.count(x)
        if a>n//2:
            return a
        if a<=n//2:
            return False
      





nums = eval(input())
y = search(nums)
print(y)



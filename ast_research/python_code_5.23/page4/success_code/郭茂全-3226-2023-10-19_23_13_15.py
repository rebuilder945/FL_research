def search(nums):
    n=len(nums)
    for x in nums:
        if nums.count(x)<=n//2:
            continue
        else:
            if x is None:
                a=False
            else:
                a=x
                return a





nums = eval(input())
y = search(nums)
print(y)



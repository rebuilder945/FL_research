def search(nums):
    n=len(nums)
    for x in nums:
        if nums.count(x)<=n//2:
            continue
        else:
            if x is not None:
                x=x
            else:
                bool(x)
    return x





nums = eval(input())
y = search(nums)
print(y)



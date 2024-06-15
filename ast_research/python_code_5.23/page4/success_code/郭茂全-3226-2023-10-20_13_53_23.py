def search(nums):
    n=len(nums)
    for x in nums:
        if nums.count(x)<=n//2:
            continue
        else:
            if x is None:
                return "False"
            else:
                x=x
                return x





nums = eval(input())
y = search(nums)
print(y)



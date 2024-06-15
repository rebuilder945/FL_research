def search(nums):
    n=len(nums)
    for x in nums:
        if nums.count(x)<=n//2:
            continue
        else:
            if x is None:
                x="False"
                return x
            else:
                return x





nums = eval(input())
y = search(nums)
print(y)



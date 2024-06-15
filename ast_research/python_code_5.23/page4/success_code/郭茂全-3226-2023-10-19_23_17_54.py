def search(nums):
    n=len(nums)
    for x in nums:
        if nums.count(x)<=n//2:
            continue
        else:
            if x is None:
                x="False"
                return a
            else:
                a=x
                return a





nums = eval(input())
y = search(nums)
print(y)



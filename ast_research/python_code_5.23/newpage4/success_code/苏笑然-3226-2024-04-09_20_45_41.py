def search(nums):
    a=len(nums)
    a=a/2
    for x in nums:
        b=nums.count(x)
        if b>a:
            return x
    else:
        y="fulse"
        return y





nums = eval(input())
y = search(nums)
print(y)



def search(nums):
    a = len(nums)
    for x in nums:
        b = nums.count(x)
        if b>a/2:
            return x
        else:
            return "False"





nums = eval(input())
y = search(nums)
print(y)



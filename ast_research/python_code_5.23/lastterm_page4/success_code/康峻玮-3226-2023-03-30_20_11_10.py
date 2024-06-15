def search(nums):
    n = len(nums)
    m=n/2
    for x in nums:
        if nums.count(x) > m:
            return x
        else:
            return "False"






nums = eval(input())
y = search(nums)
print(y)



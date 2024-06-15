def search(nums:list):
    b = len(nums)
    c = b//2
    for x in nums:
        if nums.count(x)> c:
            return x
        else:
            return False






nums = eval(input())
y = search(nums)
print(y)



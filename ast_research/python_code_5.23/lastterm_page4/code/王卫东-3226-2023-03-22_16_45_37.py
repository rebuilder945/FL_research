def search(nums:list):
    a = nums.count()
    b = len(nums)
    c = b//2
    for x in nums:
        if a > c:
            return a
        else return False






nums = eval(input())
y = search(nums)
print(y)



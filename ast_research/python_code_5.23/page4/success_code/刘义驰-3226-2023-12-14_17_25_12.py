def search(nums):
    n = len(nums)
    m = 0
    for x in nums:
        if num.count(x) > (n/2):
            m = x
        else:
            return False
    return m





nums = eval(input())
y = search(nums)
print(y)



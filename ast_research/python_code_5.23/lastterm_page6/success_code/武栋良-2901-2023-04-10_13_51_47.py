def calDegrees(nums):
    a = max(set(nums),key = nums.count)
    b = nums.count(a)
    return b
nums  =  eval(input())
c = calDegrees(nums)
def long(nums,x):
    d = nums.index(x)
    e = nums.rindex(x)
    return e-d
if c == 1:
    print(1)
else:
    for x in nums:
        if nums.count(x)==c:
            f = long(nums,x)
    print(min(f))


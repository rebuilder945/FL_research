def calDegrees(nums):
    a=0
    for n in nums:
        if nums.count(n)>a:
            a=nums.count(n)
    d=max(a)
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


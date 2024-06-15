def calDegrees(nums):
    a2=[]
    for x in nums:
        n=nums.count(x)
    if n not in a2:
        a2.append(n)
    nums=max(a2)
    return nums


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


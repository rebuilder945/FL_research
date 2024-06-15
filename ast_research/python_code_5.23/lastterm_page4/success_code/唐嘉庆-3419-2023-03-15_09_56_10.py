def calDegrees(nums):
    jack=[]
    for i in nums:
        a=nums.count(i)
    jack.append(a)
    calDegrees=max(jack)
    return calDegrees


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


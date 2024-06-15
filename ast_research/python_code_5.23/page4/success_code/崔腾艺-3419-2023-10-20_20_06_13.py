def calDegrees(nums):
    b=[]
    for i in range(len(nums)):
        f=nums[i]
        g=nums.count(f)
        b.append(g)
        d=max(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


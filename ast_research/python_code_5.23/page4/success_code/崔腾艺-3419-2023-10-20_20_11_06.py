def calDegrees(nums):
    b=[]
    for i in range(len(nums)):
        a=nums[i]
        g=nums.count(a)
        b.append(g)
        m=max(b)
    return(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


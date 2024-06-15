def calDegrees(nums):
    d=[]
    for i in nums:
        du=nums.count(i)
        d.append(du)
        a=max(d)
    return(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


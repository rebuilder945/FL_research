def calDegrees(nums):
    d=[]
    for m in nums :
        du=nums.count(m)
        d.append(du)
    return("%d"%(max(d)))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


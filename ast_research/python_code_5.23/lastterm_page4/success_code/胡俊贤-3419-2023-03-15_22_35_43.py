def calDegrees(nums):
    d=[]
    for m in nums:
        du=nums.count()
        d.append(du)
    return max(d)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


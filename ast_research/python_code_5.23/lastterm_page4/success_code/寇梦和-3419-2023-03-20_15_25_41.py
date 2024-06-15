def calDegrees(nums) :
    a=max(set(nums),key=nums.count)
    return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


def calDegrees(d):
    a=max(set(nums),key=nums.count)
    d=nums.count(a)
    return d



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


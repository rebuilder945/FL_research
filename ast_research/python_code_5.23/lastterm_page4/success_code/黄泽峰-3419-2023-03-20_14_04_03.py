def calDegrees(nums):
    a = max(set(nums),key = nums.count)
    b= nums.count(a)
    return b 


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


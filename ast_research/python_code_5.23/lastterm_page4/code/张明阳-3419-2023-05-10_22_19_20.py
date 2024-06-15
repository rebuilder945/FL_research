def calDegrees(nums):
    a=0
    for i in nums:
     if i==max(set(nums),key=nums.count)
        a+=1
    return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


def calDegrees(nums):
    du=nums.count(nums[0])
    for i in range(len(nums)):
        a= nums.count(nums[i])
        if a >= du:
            du=a
        
        return du


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


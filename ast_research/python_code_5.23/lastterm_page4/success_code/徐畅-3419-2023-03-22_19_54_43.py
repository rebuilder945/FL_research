def calDegrees(nums):
    for i in range(len(nums)):
        du=nums.count(nums[0])
        a= nums.count(nums[i])
        if a > du:
            du=a
        else:
            du=du
        return du


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


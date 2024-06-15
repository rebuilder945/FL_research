def calDegrees(nums):
    t=0;
    for i in nums:
        if nums.count(i)>t:
            t=nums.count(i);
        return t


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


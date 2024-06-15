def calDegrees(nums):
    for i in nums:
        x=0 
        if  nums.count(i)>x:
            x=nums.count(i)
        else:
            return x



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


def calDegrees(nums):
    z=0
    for x in nums:
        if nums.count(x)>z:
           z=nums,count(x)
     renturn z


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


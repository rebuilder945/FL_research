def calDegrees(nums):
    maxnum=max(nums,key=nums.count)
    d=ums.count(maxnum)
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


def calDegrees(nums):
    maxnums=max(nums,key=nums.count)
    d=nums.count(maxnums)
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


def calDegrees(nums):
 for d in nums:
    if nums.count(d)>len(nums)//2:
        return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


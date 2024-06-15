def calDegrees(nums):
 for y in nums:
    if nums.count(y)>len(nums)//2:
        return y


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


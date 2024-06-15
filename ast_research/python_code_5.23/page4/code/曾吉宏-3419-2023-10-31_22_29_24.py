def calDegrees(nums):
   ls1 = [nums.count(x) for x in nums]
return max(ls1)
    



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


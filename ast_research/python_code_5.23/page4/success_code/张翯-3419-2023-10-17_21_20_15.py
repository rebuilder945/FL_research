def calDegrees(nums):
       list=[nums.count(x) for x in range(len(nums))]
       return max(list)



       


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


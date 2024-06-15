def calDegrees(nums):
      d=0
      for i in nums:
           count=nums.count(i)
           if count>d:
               d=count
       return d
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


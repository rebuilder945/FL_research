def calDegrees():
      for i in nums:
           c=nums.count(i)
      return max(c)  
             


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


def calDegrees(nums):
       a=[]
       for x in nums:
          cnt=nums.count(x)
          a.append(x)
          c=max(a)
      return c
          
       
       
       


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


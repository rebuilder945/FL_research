def calDegrees(nums):
      s1=[]
      for x in nums:
           v1=nums.count(x)
           s1.append(v1)
     return max(s1)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


def calDegrees(d):
      d=0
      for i in nums:
            if nums.count(i)>d:
               d=nums.count(i)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


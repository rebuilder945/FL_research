def calDegrees(nums)
      a=sum(nums)
      for i in nums
      if i=a:
        d=+1
      else:
         d=+0
      return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


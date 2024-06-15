def calDegrees(nums):
      count = {}
      maximum = 0

      for i in nums:
            if not i in count:
                 count[i] = 1
            else:
                 count[i] += 1
      maximum = max(maximum, count[i])

      return maximum
nums  =  eval(input())
d=calDegrees(nums)  #调用自定义函数
print(d)
  



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


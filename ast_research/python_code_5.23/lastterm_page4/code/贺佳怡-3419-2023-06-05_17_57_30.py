def calDegrees(nums):
      maxcount=1
      for x in nums:
            c=nums.count(x)
            if c > maxcount:
                return maxcount=c
            


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


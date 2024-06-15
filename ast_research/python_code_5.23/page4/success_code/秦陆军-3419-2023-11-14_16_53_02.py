def calDegrees(nums):
   s = []
   for x in nums:
           b=nums.count(x)
           s.append(b)
   d = max(s)
   return d
            


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


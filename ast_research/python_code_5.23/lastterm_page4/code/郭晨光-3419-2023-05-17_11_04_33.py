def calDegress(nums):
      blanlis=[ ]
      for x in nums:
           m=nums.count(x)
           blanlis.append(m)
           pmax=max(blanlis)
     return pmax


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


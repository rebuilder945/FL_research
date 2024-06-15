def calDegrees(nums):
      ls=[]
      for x in nums:
           a=nums.count(x)
            ls.append(a)
      b=max(ls)
      return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


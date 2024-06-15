def calDegrees(du):
   ls=[]
   for i in nums:
      a=nums.count(i)
      ls.append(a)
      du=max(ls)
   return du


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


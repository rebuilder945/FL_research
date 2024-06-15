def calDegrees(nums):
      lst=[]
      for i in nums:
           lst.append(nums.count(i))
      b=max(lst)
      return  b



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


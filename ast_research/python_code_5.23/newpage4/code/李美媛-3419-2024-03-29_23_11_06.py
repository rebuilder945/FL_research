
  def calDegrees(nums):
      lst=[]
      for i in nums:
           lst.append(nums.count(i))
      d=max(lst)
      return  d



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


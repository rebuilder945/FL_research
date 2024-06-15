b = []
def calDegrees(nums):
      for i in nums:
           a = nums.count(i)
           b.append(a)
      calDegrees(nums) = max(b)
      


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


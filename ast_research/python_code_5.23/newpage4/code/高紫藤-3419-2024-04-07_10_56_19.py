a = []
def calDegrees(nums):
      for i in nums:
           i_count = count(i)
           a.append(i_count)
      calDegrees(nums) = max(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


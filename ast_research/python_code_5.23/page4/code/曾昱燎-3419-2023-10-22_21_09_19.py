def calDegrees(nums)
      m=[nums.count(x) for x in set(nums)]
      return max(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


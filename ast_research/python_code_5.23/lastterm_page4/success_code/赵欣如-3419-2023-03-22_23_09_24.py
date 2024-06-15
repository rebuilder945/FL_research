def calDegrees(x):
      b=[x.count(y) for y in x]
      return max(b)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


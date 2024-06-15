def calDegrees(x):
      a = []
      for i in x:
           a.append(x.count(i))
      b = max(a)
      return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


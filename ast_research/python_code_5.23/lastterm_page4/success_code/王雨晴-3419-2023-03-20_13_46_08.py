def calDegrees(x):
      n=[x.conut(x) for x in set(x)]
      return max(n)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


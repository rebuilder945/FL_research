def maxsum(y):
      y.sort()
      y.sum(split(::2))
      return y




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


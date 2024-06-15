def maxsum(x):
      x.sort()
      return sum(x[::2])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


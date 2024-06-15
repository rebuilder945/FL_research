def maxsum(x):
      s=x.sort()
      he=sum(s[:len(s)/2])
      return he





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


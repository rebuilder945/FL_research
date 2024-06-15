def maxsum(n):
   n.sort()
   m = sum(n[::2])
   return m




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


def maxsum(y):
      for i in range(len(y)):
      y.sort()
      if i%2==0:
         sum+=y
     return sum
      




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


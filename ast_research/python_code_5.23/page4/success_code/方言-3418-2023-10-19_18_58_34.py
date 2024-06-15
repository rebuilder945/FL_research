def maxsum(y):
  y.sort(reverse=False)
  sums=0
  for i in range(0,len(y),2):
    sums=sums+y[i]
    return sums




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


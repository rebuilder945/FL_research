def maxsum(y):
  y.sort(reverse=False)
  sums=0
  for i in range(len(y)):
    if i%2==0:
      sums+=y[i]
  return sums




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


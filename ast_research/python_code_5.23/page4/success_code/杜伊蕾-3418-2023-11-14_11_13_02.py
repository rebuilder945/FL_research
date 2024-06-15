def maxsum(a):
  a.sort()
  b=len(a)//2
  a=sum(a[i] for i in range(0,n*2,2))
  return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


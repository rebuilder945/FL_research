def calDegrees(a):
  b=[]
  for x in a:
    if a.count(x)>1:
      b.append(x)
      c=max(b)
      return c


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


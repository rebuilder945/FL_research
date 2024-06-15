def calDegrees(a)
  for x in range a:
    if a.count(x)>1:
      b=[]
      b.append(a)
      c=max(b)
  return c



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


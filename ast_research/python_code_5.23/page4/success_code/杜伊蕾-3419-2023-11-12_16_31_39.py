def calDegrees(a):
  for x in a:
    if a.count(x)>1:
      b=[]
      b.append(x)
      c=max(b)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


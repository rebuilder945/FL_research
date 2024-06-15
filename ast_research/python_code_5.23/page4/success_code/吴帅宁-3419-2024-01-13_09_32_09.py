def calDegrees(num):
  ls=[]
  for i in num:
    ls.append(num.count(i))
  return max(ls)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


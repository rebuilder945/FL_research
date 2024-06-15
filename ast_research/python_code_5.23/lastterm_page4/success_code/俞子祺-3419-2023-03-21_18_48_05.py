def calDegrees(x):
      len=x.count(x[0])
      for x1 in x:
            if x.count(x1)>len:
                 len=x.count(x1)
      return len



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


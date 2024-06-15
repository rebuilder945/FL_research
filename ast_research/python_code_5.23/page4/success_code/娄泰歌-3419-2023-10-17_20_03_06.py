def callDegree(ls):
      degrees=[]
      for x in ls:
           degrees.append(ls.count(x))
      d=max(degrees)
      return d



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


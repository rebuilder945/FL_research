def maxsum(x):
      x.sort()
      long=len(x)
      list1=range(1,long+1,2)
      for x1 in list1:
           a=sum(x1)
      return a
      




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


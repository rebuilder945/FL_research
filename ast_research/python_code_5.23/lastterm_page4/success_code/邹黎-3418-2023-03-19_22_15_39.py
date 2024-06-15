def maxsum(x):
      x.sort()
      total=0
      for i in range(0,len(x),2):
            total+=x[i]
      return total


       





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


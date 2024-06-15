def maxsum(ls):
   ls.sort()
   result=0
   for i in range(0,len(ls),2):
      result += ls[i]





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


total=0
def maxsum(x):
      x.sort()
      for i in range(0,len(x),2):
      total+=x[i]
      
       





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


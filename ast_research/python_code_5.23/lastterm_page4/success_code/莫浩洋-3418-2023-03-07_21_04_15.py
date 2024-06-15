def maxsum(x):
   x.sort()    
   for i in range(len(x)):
       if    i%2==0:
           b+=x[i]
   return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


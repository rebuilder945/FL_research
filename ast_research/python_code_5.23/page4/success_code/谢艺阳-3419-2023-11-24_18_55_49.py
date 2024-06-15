def calDegrees(a):
   c=[]
   for i in a:
       b= a.count(i)
       c.append(b)
   f=max(c)
   return f



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


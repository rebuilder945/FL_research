def calDegrees(a):
      length=len(a)
      m=1
      for i in range(0,length-1):
            for j in range(i+1,length):
                 if a(i)==a(j):
                     m=m+1
                     return m
    
      
       


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


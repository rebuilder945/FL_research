def calDegrees(a):   
     ls=[]
     for i in a:
          b=a.count(i) 
          ls.append(b)
     print(max(ls))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


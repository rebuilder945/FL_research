def calDegrees(x):
      a=0;
      for b in x:
           if x.count(b)>a:
              a=x.count(b);
       return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


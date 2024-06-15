def numbers(x):
     min=0;
     for y in x:
         if x.count(y)>min:
               min=x.count(y)
     return min;



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


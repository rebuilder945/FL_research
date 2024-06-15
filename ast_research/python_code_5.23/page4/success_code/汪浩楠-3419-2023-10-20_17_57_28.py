def calDegrees(a):
       c=0
       for i in a:
             if a.count(i)>c:
                 c=i
             return (c)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


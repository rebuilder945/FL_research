def calDegrees(a):
       c=0
       for i in a:
             b=a.count(i)
             if b>c:
                 c=b
       return (c)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


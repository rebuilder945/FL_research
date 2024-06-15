def calDegrees(a):
    b=0
    for i in a:
        count=a.count(i)
        if count>b:
            b=count
    return b
  


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


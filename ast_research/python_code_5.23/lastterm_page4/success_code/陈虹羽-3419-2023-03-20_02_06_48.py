def calDegrees(x):
    y=[]
    for i in x:
        a=x.count(i)
        y.append(a)
    return max(y)
  


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


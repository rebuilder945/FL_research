def calDegrees(x):
    for b in x:
    a=x.count(b)
    return a
      



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


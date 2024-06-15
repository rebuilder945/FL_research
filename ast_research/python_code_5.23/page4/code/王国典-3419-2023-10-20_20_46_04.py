def calDegrees(It):
    a=0
    for i in lt:
          if It.count(i)>a:
                a=It.count(i)
return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


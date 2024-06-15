def calDegrees(a): 
    calDegrees=max(a,key=a.count())



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


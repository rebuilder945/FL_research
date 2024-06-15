def calDegrees(y):
z=list(y)
z.sort()
x = counter(z)
 calDegrees=x
return  calDegrees



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


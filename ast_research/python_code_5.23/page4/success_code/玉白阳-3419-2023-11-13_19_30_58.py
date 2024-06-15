ls=eval(input())
x=0
for i in ls:
    if ls.count(i)>x:
        x=ls.count(i)
print(x)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


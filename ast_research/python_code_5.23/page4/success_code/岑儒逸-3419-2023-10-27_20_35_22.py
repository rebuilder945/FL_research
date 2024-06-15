def calDegrees(x):
    a=[]
    for i in x:
        a=a+x.count('i')
    return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


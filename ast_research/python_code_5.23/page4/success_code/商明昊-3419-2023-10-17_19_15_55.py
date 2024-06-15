def calDegrees(list):
    a=0
    for i in list:
        if list.count(i)>a:
            a=list.count(i)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


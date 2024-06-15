def calDegrees(a):
    n=0
    for i in a:
        if a.count(i)>n:
            n=a.count(i)
    return(n)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


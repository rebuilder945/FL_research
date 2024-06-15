def calDegrees(x):
    count=Counter(x)
    x=max(count)
    return(x)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


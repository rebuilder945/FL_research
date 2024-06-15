def calDegress(x):
    for i in x:
    
    a=len(i)/len(x)
    return max(a)
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


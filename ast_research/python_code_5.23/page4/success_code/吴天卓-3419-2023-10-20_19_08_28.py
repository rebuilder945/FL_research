def calDegrees(x):
    A=[]
    for i in x:
            A.append(x.count(i))
    return(max(A))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


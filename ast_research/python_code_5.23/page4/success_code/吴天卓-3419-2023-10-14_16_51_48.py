def calDegrees(x):
    i=0
    j=0
    A=[]
    for i in x:
        if i not in A:
            A.append(x.count(i))
    return(max(A))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


def calDegrees(n):
    lenth=len(n)
    for i in range(0,lenth+1):
        set.list=list.count(i)
    maxv=max(set.list)
    return(maxv)
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


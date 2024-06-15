def calDegrees(n):
    lenth=len(n)
    for i in range(0,lenth+1):
        everyv=n.count(i)
        listv=[everyv]
        listv2=set(listv)
    maxv=max(listv2)
    return(maxv)
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


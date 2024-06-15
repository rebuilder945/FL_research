def calDegrees(lst):
    fre=[]
    for i in lst:
        count=lst.count(i)
        fre.append(count)
    max=max(count)
    return(max)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


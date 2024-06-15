def calDegrees(list):   
    for i in list:
        a=list.count(i)
        ls2=[]
        ls2.append(a)
    return max(ls2)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


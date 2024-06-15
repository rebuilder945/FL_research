def calDegrees(n):
    list1=[]
    for x1 in n:
        a=n.count(x1)
        list1.append(a)
    return(max(list1))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


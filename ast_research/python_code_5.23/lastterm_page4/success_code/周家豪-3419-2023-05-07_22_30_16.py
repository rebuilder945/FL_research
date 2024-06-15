def calDegrees(lst):
    lst1=[]
    for x in lst:
        lst1.append(lst.count(x))
    return(max(lst1))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


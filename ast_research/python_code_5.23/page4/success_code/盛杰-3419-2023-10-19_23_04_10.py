def calDegrees(lst1):
    lst2=[]
    for i in lst1:
        lst2.append(lst1.count(i))
    d=max(lst2)
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


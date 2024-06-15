def calDegrees(list):
    list2=[]
    for i in list:
        if i not in list2:
            list2.append()
    for i in range(len(list2)):
        list2[i]=list.count(list2[i])
    return max(list2)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


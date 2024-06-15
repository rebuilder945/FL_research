def calDegrees(int):
    list=[ ]
    for i in list:
        if i not in list:
            list[i]=1
        else:
            list[i]+=1
    return list.count(list)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


def maxsum(lie):
    lis2=[]
    for x in lie:
        lis1=[]
        lis1.append(x)
        lie.remove(x)
        for y in lie:
            lis1.append(y)
            mi=min(lis1)
            lis2.append(mi)
    return max(lis2)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


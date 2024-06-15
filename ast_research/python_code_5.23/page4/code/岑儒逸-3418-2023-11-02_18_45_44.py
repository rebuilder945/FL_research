def maxsum(ls):
    ls1=[]
    ls2=[]
    ls.sort()
    for i in range(0,len(ls)-1):
        if i % 2:
            ls1.append(ls[i])
        else:
            ls2.append(ls{i})
    return sum(ls2)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


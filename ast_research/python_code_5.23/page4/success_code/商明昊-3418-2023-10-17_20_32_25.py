def maxsum(lists):
    n=2
    list=[lists[i:i+n] for i in range(0,len(lists),n)] 
    t=0
    for i in list:
        if i[0]>i[1]:
            t=t+i[1]
        else:
            t=t+i[0]
    return(t)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


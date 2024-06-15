def calDegrees(sums):
    s=0
    a=0
    list=[]
    while s<=len(sums)-1:
        for i in sums:
            if i==sums[s]:
                a+=1
        list.append(a)
        a=0
        s+=1
    return max(list)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


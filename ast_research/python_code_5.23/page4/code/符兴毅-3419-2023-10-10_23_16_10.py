def calDegrees(a) :
    for i in a:
        if i in a:
            a[i]+=1
        else i not in a:
            a[i]=1
        b=max(a)
    return b

    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


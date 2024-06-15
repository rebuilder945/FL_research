def calDegrees(a):
    a = sorted(a)
    b = []
    c=1
    for i in range(0,len(a)-1):
        if i == len(a)-1:
            if a[i]==a[i-1]:
                b.append(c+1)
        elif a[i]==a[i+1]:
            c+=1
        else:
            b.append(c)
            c=1
    if len(b)==1:
        d=b[0]
    else:
        d=max(b)
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


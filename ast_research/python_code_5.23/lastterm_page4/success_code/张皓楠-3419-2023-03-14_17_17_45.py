def calDegrees(a):
    a = sorted(a)
    b = []
    c=0
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            c+=1
        else:
            b.append(c)
            c=0
    d = max(b)
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


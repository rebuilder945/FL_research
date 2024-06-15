def  maxsum(a):
    a.sort()
    sum=0
    for x in range(len(a)):
        if x%2==0:
            sum+=a[x]
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


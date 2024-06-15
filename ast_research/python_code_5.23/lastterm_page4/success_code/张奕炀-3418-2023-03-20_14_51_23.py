def maxsum(a):
    b=[]
    k=0
    c = 0
    for i in range(int(len(a)/2)):
        b.append(a[k:(k+2)])
        k+=2
    for j in range(len(b)):
        c += min(b[j])
    return c




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


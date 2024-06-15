def maxsum(n):
    n.sort()
    a=len(n)//2
    max=0
    for i in range(n):
        max=max+n[2*i]
    return(max)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


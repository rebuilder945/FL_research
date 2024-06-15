def maxsum(a):
    a.sort()
    n=0
    s=0
    for x in a:
        if n%2==0:
            s+=x
        n+=1
    return s




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


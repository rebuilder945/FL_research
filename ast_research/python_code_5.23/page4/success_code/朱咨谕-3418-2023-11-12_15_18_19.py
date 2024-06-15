def maxsum(a):
    a.sort()
    i=len(a)-1
    while i>=1:
        a.pop(i)
        i-=2
    return sum(a)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


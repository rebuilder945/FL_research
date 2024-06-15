def maxsum(nums):
    x=sorted(nums)
    h=0
    for i in range(0,len(x),2):
        h+=x[i]
    return h




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


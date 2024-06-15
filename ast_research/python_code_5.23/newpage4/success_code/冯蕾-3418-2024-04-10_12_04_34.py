def maxsum(lst):
    sum=0
    lst.sort()
    a=len(lst)
    for i in range(0,a,2):
        sum+=lst[i]
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


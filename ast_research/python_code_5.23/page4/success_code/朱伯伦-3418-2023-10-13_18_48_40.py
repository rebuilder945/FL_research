def maxsum(list):
    list.sort()
    n=len(list)//2
    sum=0
    for i in range(n):
        sum+=list[2*i]
    return sum





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


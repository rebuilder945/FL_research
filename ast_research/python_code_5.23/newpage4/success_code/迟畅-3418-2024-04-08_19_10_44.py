def maxsum(lst):
    lst.sort()
    sum=0
    for i in range(len(lst)):
        if i%2==0:
           sum=sum+lst[i]
    return sum





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


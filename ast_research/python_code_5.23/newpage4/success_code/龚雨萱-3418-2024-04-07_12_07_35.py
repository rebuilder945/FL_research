def maxsum(list):
    list.sort()
    sum=0
    for i in range(len(list)):
        if i%2==0:
            sum=sum+list[i]
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


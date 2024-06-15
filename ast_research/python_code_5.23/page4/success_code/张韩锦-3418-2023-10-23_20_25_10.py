def maxsum(lst1):
    lst1.sort()
    sum=0
    for i in range(len(lst1)):
        if i%2==0:
            sum=sum+lst1[i]
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


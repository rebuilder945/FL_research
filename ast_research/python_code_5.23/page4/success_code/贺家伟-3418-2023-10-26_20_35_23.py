def maxsum(n):
    sum=0
    n.sort(reverse=True)
    for i in range(1,len(n),2):
        sum=sum+int(n[i])
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


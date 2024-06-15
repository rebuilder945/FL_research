def maxsum(n):
    sum=0
    n.sort()
    for i in range(len(n)):
        if i%2==0:
            sum+=n[i];
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


def maxsum(liebiao):
    sum = 0
    liebiao.sort(reverse=False)
    N = len(liebiao)
    n = N*0.5
    for i in range(N):
        if i%2==0:
            sum+=liebiao[i]
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


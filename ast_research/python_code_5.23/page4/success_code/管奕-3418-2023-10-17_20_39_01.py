def maxsum(a):
    maxsum=0
    for i in range(a):
        b=int(i)
        if b%2==0:
            maxsum+=i




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


def maxsum(n):
    import random
    b=[]
    minSum=0
    for a in range(len(n)):
        a=random.sample(n,2)
        b=min(a)
        minSum+=b
    return max(minSum)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


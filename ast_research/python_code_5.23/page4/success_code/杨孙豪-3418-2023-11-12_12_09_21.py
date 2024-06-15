def maxsum(x):
    c=0
    for i in range(len(x)//2):
        bst=[x[2*i-1],x[2*i]]
        c=c+min(bst)
    return c




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


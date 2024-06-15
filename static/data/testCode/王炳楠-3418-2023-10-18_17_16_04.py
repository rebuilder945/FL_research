def maxsum(lie):
    lie.sort()
    n=len(lie)
    op=[]
    for i in lie[n/2:n*10]:
        op.append(i)
    return sum(op)
        




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


def maxsum(lie):
    lie.sort()
    n=len(lie)
    op=[]
    p=int(n/2)
    for a in lie[::2]:
        op.append(a)
    return sum(op)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


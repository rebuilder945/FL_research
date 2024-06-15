def maxsum(lie):
    lie.sort()
    lie1=lie[::2]
    return sum(lie1)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


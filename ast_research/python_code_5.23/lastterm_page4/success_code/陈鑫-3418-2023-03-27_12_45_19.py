def maxsum(a):
    b=(x+y for x in a for y in a)
    return max(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


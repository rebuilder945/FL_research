def maxsum(m):
    h=[]
    m.sort
    for i in m[::2]:
        h.append(i)
    return sum(h)
nums  =  eval(input())




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


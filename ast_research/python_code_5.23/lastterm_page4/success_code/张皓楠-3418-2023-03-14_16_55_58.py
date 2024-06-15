def maxsum(a):
    a = sorted(a)
    b = []
    for i in range(0,len(a),2):
        b.append(a[i])
    c = sum(b)
    return c




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


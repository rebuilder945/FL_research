def maxsum(a):
    a.sort()
    a.reverse()
    c=0
    for x in range(1,len(a),2):
        c+=a[x]
    return c




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


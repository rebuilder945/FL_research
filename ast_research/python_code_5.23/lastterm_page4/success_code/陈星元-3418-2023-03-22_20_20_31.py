def maxsum(a):
    a.sort(reverse=True)
    b=0
    for x in range(1,len(a),2):
        b=b+a[x]
    return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


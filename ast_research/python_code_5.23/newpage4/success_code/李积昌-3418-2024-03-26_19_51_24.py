def maxsum(a) :
    a.sort()
    h=0
    for x in range(0,len(a),2):
        h+=a[x]
    return h





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


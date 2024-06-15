def maxsum(a):
    b=sorted(a)
    c=0
    for i in range(0,len(a),2):
        c+=b[i]




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


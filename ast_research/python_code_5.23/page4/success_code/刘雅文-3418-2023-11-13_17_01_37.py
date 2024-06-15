def maxsum(a):
    a.sort()
    
    b=sum(a[i] for i in range(0,len(a),2))
    return b 




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


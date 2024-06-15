def maxsum(n):
    n.sort()
    
    total = 0
    for i in n[0:-1:2]:
        total+= i
    return total





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


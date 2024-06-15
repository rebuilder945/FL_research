def maxsum(n):
    n.sort()
    b = n[0: int(len(n)/2)]
    total = 0
    for i in b:
        total+= i
    return total





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


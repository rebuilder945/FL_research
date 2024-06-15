def  maxsum(num):
    num.sort()         
    a = num[0::2]
    b = sum(a)
    return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)


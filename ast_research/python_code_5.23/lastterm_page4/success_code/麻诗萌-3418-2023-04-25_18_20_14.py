def maxsum(data) :
    data.sort()
    lst=data[::2]
    return sum(lst)
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

